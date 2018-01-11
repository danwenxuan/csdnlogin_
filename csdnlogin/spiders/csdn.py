# -*- coding: utf-8 -*-
import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://passport.csdn.net/account/login?from=http://write.blog.csdn.net/postlist',
               "http://my.csdn.net/my/mycsdn"]

    def __init__(self):  # 初始化
        self.browser = None
        self.cookies = None
        super(CsdnSpider, self).__init__()  # 传递给父类
        # dispatcher.connect(self.spider_closed,signals.spider_closed)#爬虫关闭通过信号调用我们自己的函数

    def spider_closed(self,response):
        print("爬虫关闭")
        self.browser.close()



    def parse(self, response):
        #打印链接 ，打印网页源代码
        print("parse-----------------------------")
        print(response.url)
        print(response.body.decode("utf-8","ignore"))