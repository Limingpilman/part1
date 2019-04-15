# -*- coding: utf-8 -*-
import scrapy
from ..items import SatfItem

class GetSpider(scrapy.Spider):
    name = 'get'
    allowed_domains = ['www.offcn.com']
    start_urls = ['http://www.offcn.com/yixue/2018/0105/32099.html']

    def parse(self, response):
        item = SatfItem()
        item['name'] = response.xpath('//title/text()').extract()
        item['text'] = response.xpath('//li/a/text()').extract()
        print(item)
        return item

