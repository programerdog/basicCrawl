#!/usr/bin/env python
#coding:utf-8
from DataOutPut import DataOutPut
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from urlManager import urlManager
class SpiderMain(object):
    def __init__(self):
	    self.manager=urlManager()
	    self.parser=HtmlParser()
	    self.downloader=HtmlDownloader()
	    self.output=DataOutPut()
    def crawl(self,root_url):
	    self.manager.add_new_url(root_url)
	    while(self.manager.has_new_url() and self.manager.old_url_size()<100):
	   	 try:
	   	         new_url = self.manager.get_new_url()
	   	         html = self.downloader.download(new_url)
	   	         new_urls,data=self.parser.parser(new_url,html)
	   	         self.manager.add_new_urls(new_urls)
	   	         self.output.store_data(data)
	   	         print('have got %s urls:'%self.manager.old_url_size())
	   	 except:
		   	 print('crawl failed')
	    self.output.output_html()

if __name__=="__main__":
	spider_main = SpiderMain()
	spider_main.crawl("https://baike.baidu.com/view/284853.htm")
	
	 
