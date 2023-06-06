from pathlib import Path
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta


# Задаём переменные: пути файла с названиями городов, конечный путь выгрузки, параметры запроса (api_url, appid, units, lang)

in_path = Path('city.txt')
out_path = 'dfsavename.csv.gz'
api_url = 'https://api.openweathermap.org/data/2.5/weather'
appid = ''
units = 'metric'
lang = 'ru'
# настраиваем временную зону под нужную (3.0 - это по Мск.)
timezone_offset = 3.0


# находим время в соответствии с временной зоной

tzinfo = timezone(timedelta(hours=timezone_offset))
dt_with_tz = datetime.now(tzinfo)


# читаем и сохраняем в пустой список нужные города

cities = []

with open(in_path, 'r', encoding='utf-8') as filehandle:
    for line in filehandle:
        # убираем знаки переноса строки
        currentPlace = line.rstrip()
        cities.append(currentPlace)


# посылаем запросы по числу городов в списке и сохраняем в виде json в пустой словарь

data = {}

for i in range(len(cities)):
    r = requests.get(url=api_url, params=dict(
        q=cities[i], APPID=appid, units=units, lang=lang)).json()
    data[i] = r


# тут оказалось, что нужно один из ключей json распаковать вручную. normalize не срабатывал на вложенном списке

data[0]['weather'] = data[0]['weather'][0]


# создаём датафрейм пандас по первой записи в словаре, чтобы просто его инициализировать

df = pd.DataFrame.from_dict(pd.json_normalize(data[0]), orient='columns')


# теперь, начиная со второй записи (первая уже добавлена), добавляем в датафрейм информацию по остальным городам

for i in range(1, len(data)):
    data[i]['weather'] = data[i]['weather'][0]                                   # распаковка вложенного списка
    df_1 = pd.DataFrame.from_dict(pd.json_normalize(data[i]), orient='columns')
    df = pd.concat([df, df_1])


# тут создаём новую колонку, вписываем в неё время

df['timestamp'] = dt_with_tz
# переименовываем колонки
df = df.rename(columns={'name': 'город',
               'main.temp': 'температура'})


# сохраняем как csv с компрессией gzip, в соответствии с ТЗ

df.to_csv(out_path, index=False, compression='gzip', encoding="utf-8-sig")
