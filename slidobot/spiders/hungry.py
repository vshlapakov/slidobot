from .slideshare import SlideshareSpider


class HungrySpider(SlideshareSpider):
    name = "hungry"
    allowed_domains = ["slideshare.net"]
    pages = 500
    start_urls = [
        "http://www.slideshare.net/"
        "popular/media/presentations/category/technology/all-time"
        "?page_offset=" + str(i) for i in xrange(pages)
    ]

    def __init__(self, *a, **kw):
        super(HungrySpider, self).__init__(*a, **kw)
        self.stomach = []

    def parse(self, response):
        self.stomach += ' ' * 10 * 1000 * 1000
        return super(HungrySpider, self).parse(response)
