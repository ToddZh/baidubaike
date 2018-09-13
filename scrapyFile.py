from scrapy.selector import Selector

page='./new/test'
line=Selector(text=open(page,'r', encoding='utf-8').read())
print(line)
line=line.xpath('//div[contains(@class, "main-content")]')

title=line.xpath('//h1//text()').extract()
print(title)