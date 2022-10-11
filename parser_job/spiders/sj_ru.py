import scrapy
from scrapy.http import HtmlResponse
from parser_job.items import ParserJobItem


class SjRuSpider(scrapy.Spider):
    name = 'sj_ru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vakansii/analitik.html?geo%5Bt%5D%5B0%5D=4']

    def parse(self, response:HtmlResponse):
        #next_page = response.xpath("//a[@rel='next']/@href").get()
        #if next_page:
         #   yield response.follow(next_page, callback=self.parse)


        vacancies_links = response.xpath("//span[@class='_9fIP1 _249GZ _1jb_5 QLdOc']//@href").getall()
        for link in vacancies_links:
            yield response.follow(link, callback=self.parse_vacancy)


    def parse_vacancy(self, response:HtmlResponse):
        vacancies_name = response.css("h1::text").get()
        vacancies_url = response.url
        vacancies_salary = response.xpath("//span[@class='_2eYAG _1nqY_ _249GZ _1dIgi']//text()").getall()

        print(f'\n*******************************#\n{vacancies_name}\n{vacancies_url}\n{vacancies_salary}\n*******************************\n')

        yield ParserJobItem(
            name = vacancies_name,
            url = vacancies_url,
            salary = vacancies_salary

        )

