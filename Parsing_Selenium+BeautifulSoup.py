# подгрузка библиотек
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # устанавливаем и инициализщируем драйвер селениума
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # указываем адрес страницы в гет-запросе, на которой будем работать - сайт врачей Томска
    # нужно собрать Специальность, Стаж, Место работы, Рейтинг
    driver.get("https://tomsk.zoon.ru/p-doctor/")
    # экземпляр класса для автоматизированного взаимодействия с элементами страницы
    acti = ActionChains(driver)
    # с помощью метода класса действий (переместить к элементу) перемещаем условный курсор к
    # элементу по выбранному селектору (название элемента и класса смотрим в исходном коде страницы)
    acti.move_to_element(driver.find_element(By.CSS_SELECTOR, 'span.js-next-page'))
    # команда, необходимая для старта ранее заданного действия
    acti.perform()
    # задаём в переменную экз. класса ожидания для удобства
    wait = WebDriverWait(driver, timeout=10)
    # так как  однотипных действий, которые пойдут далее, довольно много, то задаём бесконечный цикл
    # выполнения следующих команд
    while True:
        # ожидание до тех пор, пока подгрузчик страницы не исчезнет (пока видимый)
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, 'div.js-loading-box')))
        # ожидание до тех пор, пока элемент, прописанный в параметрах, не станет видимым
        # элемент - кнопка "Показать еще", название селектора берется в исхдном коде страницы
        # сразу применяем метод Клик к объекту, как только он появится
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.js-next-page'))).click()
# на случай, если что-то пошло не так, выводим ошибку
except Exception as ex:
    print(f'Error: {ex}')
# записываем в переменную исходный код драйвера, в котором, после кода выше, должен загрузиться
# весь код страницы с нужными нам подгрузками карточек врачей
html = driver.page_source
# команда прекращения работы драйвера
driver.quit()

# начинаем обработку кода страницы, импортируем суп и цсв для записи итоговой таблицы
from bs4 import BeautifulSoup
import csv

# создаём суп-объект из исходного кода, пропуская через парсер
soup = BeautifulSoup(html, 'lxml')
# селектором выбираем сначала весь лист специалистов, затем последовательность всех карточек
# специалистов, указывая соответствующие тэги и классы, найденные на странице
cards_list = soup.select_one('div.js-specialist')
cards_all = cards_list.select('div.js-results-item')
# создаём пустой итоговый список
spec_inf_list = []
# цикл для прохода по всем карточкам, взятым из предидущего селектора
for cards in cards_all:
    # для каждой карточки из списка карточек...
    # находим специальность по тегу и классу, выбираем селектором все записи
    spec_list = cards.select('div.prof-spec-list a')
    # в полученном списке кода, для каждой записи извлекаем текст,
    # результирующий список джойним, через запятую (специальностей может быть больше одной)
    spec_list2 = ','.join([i.text for i in spec_list])
    # опыт выбираем селектором первого вхождения, по найденным тегам и классу опыта в коде
    spec_exp = cards.select_one('div.specialist-experience span')
    # если опыт не указан, то пустая строка, если указан, то идёт проверка на число
    # если написана вместо опыта какая-то лабуда, то заменяем её пустой строкой
    # в противном случае извлекаем текст, убираем пробелы, сплитим в список и берём второй эелемент
    if not spec_exp:
        spec_exp = ''
    else:
        spec_exp = spec_exp.text.strip().split()[1]
        if spec_exp.isdigit():
            spec_exp = spec_exp
        else:
            spec_exp = ''
    # место работы по селектору всего с укзанием соотв. тега и классов
    # пришлось уточнить параметры селектора, так как через один и тот же класс в исходном
    # коде записано как место работы, так и адрес, который не нужен
    spec_place = cards.select('div.specialist-place a.specialist-place-name')
    # выбираем текст, убираем пробелы для каждой записи в селекторе, джойним через запятую
    # так как в записи может быть указано несколько мест работы
    spec_place2 = ','.join([i.text.strip() for i in spec_place])
    # затычка, на случай, если места указаны не перечислением через запятую, а выпадающим
    # списком. Тогда берём более расширенные параметры селектора, собираем все данные,
    # в том числе может попасться и адрес
    if not spec_place2:
        spec_place = cards.select('div.specialist-place a')
        spec_place2 = ','.join([i.text.strip() for i in spec_place])
    # рейтинг по одиночному селектору, тэг, класс найден в исходном коде
    spec_raiting = cards.select_one('div.stars-view span')
    # если рейтинга нет (пустой), то пустая строка, если нет - извлекам текст
    if not spec_raiting:
        spec_raiting = ''
    else:
        spec_raiting = spec_raiting.text
    # добавляем словарь из поулченных переменных для каждой карточки специалиста в итоговый список
    # прописываем ключи для каждой переменной
    spec_inf_list += [{
        'Specialization': spec_list2,
        'Experience': spec_exp,
        'Workplace': spec_place2,
        'Raiting': spec_raiting
        }]
# заводим переменную ключей для итогового файла
keys = spec_inf_list[0].keys()
# записываем получившийся список словарей по ключам в файл tomsk_med_inf.csv
with open('tomsk_med_inf.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    for i in spec_inf_list:
        dict_writer.writerow(i)
# принтим посмотреть список словарей
print(spec_inf_list)
