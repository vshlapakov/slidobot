Slidobot
======

Slidobot is a tiny Scrapy project for scraping presentations info from [Slideshare](www.slideshare.net).

This project is only meant for educational purposes.

Spiders
-----
The project contains 2 spiders:
- `slideshare` - simple spider for scraping data from selection grid
- `slideshare_full` - advanced similar spider which parses every slide page separately (so we can get expanded description for each entry).

How-To
-----
Project based on this [Scrapy](http://doc.scrapy.org/en/latest/intro/tutorial.html) tutorial.
You can specify crawling pages urls in spider source file (`start_urls` var).

By default it's `http://www.slideshare.net/popular/media/presentations/category/technology/all-time` page
(you can get such url using Explore part of service and applying different filters).

Properly speaking, it's possible to use any Explore filter url for crawling.

Page number is set at the same place (`start_urls` var).

For running spider call `scrapy crawl slideshare` or `scrapy crawl slideshare_full`.
