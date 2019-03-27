import scrapy


class economy_gov_kz_news_en(scrapy.Spider):
    name = "economy_gov_kz_news_en"

    def start_requests(self):
        # read urls from a file
        with open("./economy.gov.kz_urls_en.txt") as urls_file:
            urls = urls_file.read().splitlines()

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url - response.url
        # kaz-url - "http://economy.gov.kz" + response.css("ul.language-switcher-locale-url li.kk a::attr(href)").get()
        # title - response.css("h1.title::text")[-1].getall()
        # date-time - response.css("div.submitted::text").getall()
        # text - response.css("div.field-item p::text").getall()

        yield {
            "url": response.url,
            "kaz-url": "http://economy.gov.kz"
            + response.css(
                "ul.language-switcher-locale-url li.kk a::attr(href)"
            ).get(),
            "title": response.css("h1.title::text")[-1].getall(),
            "date-time": response.css("div.submitted::text").getall(),
            "text": response.css("div.field-item p::text").getall(),
        }
