from scrapy import Spider #to crawl the website
import scrapy
from scrapy.selector import Selector #to select the html tags
from stack.items import StackItem #to import the class from items.py
class StackSpider(scrapy.Spider):
    name = "stack" #name of spider
    allowed_domains = ["stackoverflow.com"]  #base url for spider to crawl
    start_urls = ["https://stackoverflow.com/questions?tab=Newest",] #starting url
    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="s-post-summary--content"]') #xpath to select the all questions cuz grab all h3 elements children of div and class name is s-post-summary--content
        for question in questions:
            item=StackItem()
            item['title']=question.xpath('h3[@class="s-post-summary--title"]/text()').extract()[0] #extract the text from the a tag 
            item['url']=question.xpath('h3/a[@class="s-link"]/@href').extract()[0] #extract the href from the a tag
            #these two steps as we need to extract the title and url of the question in stackoverflow
            yield item