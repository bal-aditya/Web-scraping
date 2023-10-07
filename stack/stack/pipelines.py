# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter #it is used to convert the item to dict
import pymongo #to connect to mongodb
from scrapy import settings #to get the settings.py file
from scrapy.exceptions import DropItem #to drop the item if it is duplicate
from scrapy import log # it is used to log the error 

class MongoDBPipeline(object):
    def __init(self):
        conn=pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db=conn[settings['MONGODB_DB']]
        self.collection=db[settings['MONGODB_COLLECTION']]
    def process_item(self, item, spider):
        valid=True
        for data in item: #to check if the item is empty or not
            if not data: 
                valid=False
                raise DropItem("Missing {0}!".format(data)) #if the item is empty then drop the item ,format is used to convert the data to string
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",level=log.DEBUG, spider=spider) #to log the message if the item is added to mongodb
        return item
