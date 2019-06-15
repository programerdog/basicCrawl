#!/usr/bin/env python
#coding:utf-8
class urlManager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def has_new_url(self):
        '''
        if there is unused url
        :return:
        '''
        return self.new_url_size()!=0
    def get_new_url(self):
        '''
        get a url that is not used
        :reutn:
        '''
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        
    def add_new_url(self,url):
        '''
        add new url to new_urls
        :param url:single url
        :return:
        '''
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls):
        '''
        add new urls to new_urls
        :param urls:url set
        :return
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        '''
        get size of new_urls
        :return:
        '''
        return len(self.new_urls)
    def old_url_size(self):
        '''
        get size of old_urls
        :return:
        '''
        return len(self.old_urls)

#if __name__=="__main__":
#    obj1 = urlManager()
#    obj1.urlMangerTest();
#
