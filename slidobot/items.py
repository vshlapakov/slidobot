from scrapy.item import Item, Field


class SlideItem(Item):
    title = Field()
    author = Field()
    url = Field()
    info = Field()


class FullSlideItem(SlideItem):
    views = Field()
    desc = Field()
