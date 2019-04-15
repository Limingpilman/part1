import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

product = Product(name ='sasdf',price = 107890)
##print(product)
product.get('lala','unknow field')
t = product.get('name','afd')
print(t)