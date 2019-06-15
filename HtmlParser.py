#coding:utf-8
import re
from urllib import parse 
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        '''
        analysis page content and get URL data
        :param page_url:url you want to download
        :param html_cont:text of url content
        :return:return url and data
        '''
        if page_url is None or html_cont is None:
            return
        new_urls=self._get_new_urls(page_url,html_cont)
        new_data=self._get_new_data(page_url,html_cont)
        return new_urls,new_data
    def _get_new_urls(self,page_url,html_cont):
        '''
        get new url set
        :param page_url:downloader page url
        :param html_cont:html content
        :return :return new url set
        '''
        new_urls = set()
        pattern = re.compile(r'(?<=href=").+?(?=" data-lemmaid)')
        links = re.findall(pattern,html_cont)
        for link in links:
            #get whole url
            new_full_url = parse.urljoin(page_url,link)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,html_cont):
        '''
        get useful data
        :param page_url:downlosder page url
        :param heml_cont:html content
        :return :return useful data
        '''
        data={}
        data["url"] = page_url
        pattern = re.compile(r'(?<=<dd class="lemmaWgt-lemmaTitle-title">\n<h1>).+?(?=</h1>)')
        title = re.findall(pattern,html_cont)
        data["title"]=title
        soup = BeautifulSoup(html_cont,"html.parser")
        summary=soup.find("div",class_="lemma-summary")
        data["summary"]=summary.get_text()
        return data


#if __name__=="__main__":
#    a=HtmlParser()
