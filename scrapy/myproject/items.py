from scrapy_djangoitem import DjangoItem

from product.models import Product

import scrapy

class KnifekitsDJItem(DjangoItem):
    django_model = Product
    sku = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()


class CkkItem(scrapy.Item):
    
    crawl_date = scrapy.Field()
    date_str = scrapy.Field()
    description= scrapy.Field()
    desc_text = scrapy.Field()
    price = scrapy.Field()
    sku = scrapy.Field()
    metaKeywords = scrapy.Field()
    breadcrumbs = scrapy.Field()
    image = scrapy.Field()
    images = scrapy.Field()
    link = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()
    name = scrapy.Field()
    shop = scrapy.Field()
    image_paths=scrapy.Field()



class RedditItem(scrapy.Item):
    '''
    Defining the storage containers for the data we
    plan to scrape
    '''
    date = scrapy.Field()
    date_str = scrapy.Field()
    sub = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    commentsUrl = scrapy.Field()