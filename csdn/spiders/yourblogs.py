# -*- coding: utf-8 -*-
import scrapy
import bs4
from bs4 import BeautifulSoup
from csdn import items
from scrapy.linkextractors import LinkExtractor #提取链接
from  scrapy.spiders import CrawlSpider,Rule #循环抓取规则


class YoublogsSpider(CrawlSpider):
    name = 'yourblogs'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/yincheng01/article/list/1']
    rules = (
        Rule(LinkExtractor(allow=r"/yincheng01/article/list/\d+"), process_links="parse_links"),  # 自动翻页，没有callback自动翻页
        Rule(LinkExtractor(allow=r"/article/details/\d+"), callback="parse_content"),  # 子链接
    )

    def parse_links(self, links):  # 没有callback,自动加上process_links系统默认
        print(links)
        return links

    def parse_content(self, response):
        data=response.body#内容
        soup=BeautifulSoup(data,"html5lib")#解析方式

        csdnitem=items.CsdnItem()
        csdnitem["title"]=soup.find("h1", "csdn_top").get_text()

        csdnitem["url"] =response.url

        if  None==soup.find("div", "markdown_views"):
            if  None!=soup.find("div",id="article_content"):
                csdnitem["content"] =soup.find("div",id="article_content").get_text()
        else:
            csdnitem["content"]=soup.find("div", "markdown_views").p.get_text()
        yield csdnitem
















