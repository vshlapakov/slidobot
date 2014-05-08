from scrapy.item import Item, Field


class SlideItem(Item):
    title = Field()
    author = Field()
    url = Field()
    info = Field()


class FullSlideItem(Item):
    title = Field()
    author = Field()
    url = Field()
    views = Field()
    desc = Field()
