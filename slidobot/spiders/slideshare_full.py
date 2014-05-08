from urlparse import urljoin

from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from slidobot.items import FullSlideItem


class SlideshareFullSpider(Spider):
    name = "slideshare_full"
    allowed_domains = ["slideshare.net"]
    pages = 1
    start_urls = [
        "http://www.slideshare.net/"
        "popular/media/presentations/category/technology/all-time"
        "?page_offset=" + str(i) for i in xrange(pages)
    ]

    def parse(self, response):
        """
        @url http://www.slideshare.net/popular/media/presentations/
            category/technology/all-time?page_offset=2
        @returns items 0 0
        @returns requests 0 1
        """

        sel = Selector(response)
        slides = sel.xpath('//div[@class="details"]')
        items = []

        for slide in slides:
            title = slide.xpath('a[contains(@class, "title")]')
            path = title.xpath('@href').extract()
            if path:
                url = urljoin(response.url, path[0])
                yield Request(url, callback=self.parse_slidepage)

    def parse_slidepage(self, response):
        """
        @url www.slideshare.net/jbellis/state-of-cassandra-2011
        @returns items 0 1
        @returns requests 0 0
        @scrapes title author url views desc
        """

        sel = Selector(response)
        articles = sel.xpath('//article/div/div')
        items = []

        for article in articles:
            item = FullSlideItem()
            common = article.xpath('div/div[@class="title"]')
            item['title'] = common.xpath('h1/text()').extract()
            item['author'] = common.xpath('h2/a/text()').extract()
            item['url'] = [unicode(response.url)]
            item['views'] = common.xpath('ul/li/span/text()').extract()

            desc = article.xpath('p[contains(@class, "descriptionExpanded")]')
            item['desc'] = desc.xpath('normalize-space(text())').extract()

            items.append(item)

        return items
