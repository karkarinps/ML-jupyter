# импортируем библиотеки, создаём скрапи-проект в командной строке, создаём файл-паук в папке spiders
import scrapy
import time

# задаём класс, наследуем от класса паука скрапи, задаём имя паука
class FirstSpider(scrapy.Spider):
    name = 'FirstSpider'
    # задаём стартовый урл (книжный магазин), можно задать несколько для распараллеливания сбора
    # требуемые данные: название книги, цена и жанр
    start_urls = ["http://knigi.tomsk.ru/products/new"]
    # напишем функцию парс с параметром респонс, который принимает ответ от гет-запроса
    # функция будет собирать ссылки со страницы на которой находится по селектору-аттрибуту,
    # затем переходить методом фолоу по каждой ссылке и выполнять функцию из параметра, которую
    # напишем ниже, затем будет получать адрес следующей страницы по селектору-аттрибуту и
    # переходить на неё. Далее рекурсия: сбор ссылок с новой страницы, переход, выполнение.
    def parse(self, response):
        # собираем список ссылок со страницы, по всем соотв. аттрибутам
        # исходный код находится в объекте response
        links = response.css("div.name a::attr(href)")
        # переходим по каждой ссылке, задаём время ожидания 2 сек между запросами, чтобы не сойти за бота
        for i in links:
            time.sleep(2)
            # переходим по ссылке follow и выполняем функцию parse_book
            yield response.follow(i, self.parse_book)
        # присваиваем переменной ссылку на следующую страницу, которую находим по селектору из исходного кода
        next_page = response.css("div.pagination a::attr(href)")[-1].get()
        # переходим на новую страницу и выполняем саму же эту функцию
        yield response.follow(next_page, self.parse)
    # функция для сбора нужной инфы с каждой страницы-книги, на которую переходим (название книги,
    # цена и жанр). Данные запишем в виде словарей
    def parse_book(self, response):
        yield {
        'book_name': response.css('div.page h1::text').get(),
        'book_price': response.css('div.price::text').get().split()[0],
        'book_genre': response.css('div.breadcrumbs ul li a::text')[-1].get()
        }
# далее в терминале папки spider запустим паука командой, указав его название и название и формат
# файла вывода собранной информации:
# scrapy runspider 'First_spider.py' -o'Books_inf.csv'