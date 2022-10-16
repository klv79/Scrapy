import scrapy
from scrapy.http import HtmlResponse
from castoparser.items import CastoparserItem

class CastoSpider(scrapy.Spider):
    name = 'casto'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/gardening-and-outdoor/garden-decoration-and-improvement/']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@class='product-card__img-link']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").get()
        price = response.xpath("//span[@class='price']/span/span/text()").get()
        photo = response.xpath("//div[@class='js-zoom-container']/img/@data-src").getall()
        photo_link = f'https://www.castorama.ru{photo[0]}'
        yield CastoparserItem(name=name, price=price, photos=photo_link)



