# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import datetime, os
import scrapy
from urllib.parse import urlparse
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class CkkImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return 'ckk/HS/' + os.path.basename(urlparse(request.url).path)
    def get_media_requests(self, item, info):
        for image_url in item['images']:
            yield scrapy.Request("https://knifekits.com/vcom/" +image_url)
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item has no images")
        adapter = ItemAdapter(item)
        adapter['image_paths'] = image_paths
        return item

class MongoPipeline(object):
    collection_name = 'crawls'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item