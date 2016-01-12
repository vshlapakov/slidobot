from urlparse import urljoin

from scrapy.spider import Spider
from scrapy.selector import Selector

from slidobot.items import SlideItem


class SlideshareSpider(Spider):
    name = "slideshare"
    allowed_domains = ["slideshare.net"]
    pages = 100
    start_urls = [
        "http://www.slideshare.net/"
        "popular/media/presentations/category/technology/all-time"
        "?page_offset=" + str(i) for i in xrange(pages)
    ]

    def parse(self, response):
        """ SlideSpider contract

        @url http://www.slideshare.net/popular/media/presentations/
            category/technology/all-time?page_offset=2
        @returns items 0 18
        @returns requests 0 0
        @scrapes title author url info
        """

        sel = Selector(response)
        slides = sel.xpath('//div[@class="details"]')
        items = []

        for slide in slides:
            item = SlideItem()

            author = slide.xpath('div[contains(@class, "author")]/'
                                 'a[contains(@class, "j-author_text")]')
            item['author'] = author.xpath('text()').extract()

            title = slide.xpath('a[contains(@class, "title")]')
            item['title'] = title.xpath('normalize-space(text())').extract()

            path = title.xpath('@href').extract()
            item['url'] = [urljoin(response.url, rel) for rel in path]

            item['info'] = slide.xpath('normalize-space('
                                       'div[@class="info"]/text())').extract()
            items.append(item)

        return items
