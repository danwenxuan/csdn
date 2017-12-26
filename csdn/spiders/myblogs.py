# -*- coding: utf-8 -*-
import scrapy
import bs4
from bs4 import BeautifulSoup
from csdn import items


class MyblogsSpider(scrapy.Spider):
	name = 'myblogs'
	allowed_domains = ['blog.csdn.net']
	offset = 1
	start_urls = ['http://blog.csdn.net/yincheng01/article/list/1']

	def parse(self, response):
		data = response.body  # 内容
		soup = BeautifulSoup(data, "html5lib")  # 解析方式
		# 提取
		datalist = soup.find_all("div", "list_item article_item")
		print(datalist, "datalist")
		# print(datalist)
		for line in datalist:
			csdnitem = items.CsdnItem()
			csdnitem["title"] = line.find("span", "link_title").a.get_text()
			csdnitem["url"] = line.find("span", "link_title").a.get("href")
			csdnitem["content"] = line.find("div", "article_description").get_text()
		yield csdnitem

		if self.offset < 72:
			self.offset += 1
			yield scrapy.Request("http://blog.csdn.net/yincheng01/article/list/" + str(self.offset),
								 callback=self.parse)
