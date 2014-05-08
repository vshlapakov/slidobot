from scrapy.item import Item, Field


class SlideItem(Item):
    name = Field()
    author = Field()
    url = Field()
    info = Field()
