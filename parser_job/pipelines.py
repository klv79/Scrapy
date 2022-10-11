# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import collections
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ParserJobPipeline:
    def __init__(self):
        client = MongoClient('localhost:27017')
        self.mongo_db = client.parser_job


    def process_item(self, item, spider):
        collections = self.mongo_db[spider.name]
        collections.insert_one(item)
        print(
            f'\n*******************************#\n{item}\n{spider}\n*******************************\n'
        )

        return item
