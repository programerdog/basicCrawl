#coding:utf-8
import requests
import chardet
class HtmlDownloader(object):
    def download(self,url):
        '''
        down load html from url
        '''
        if url is None:
            return None
        s=requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.146 Safari/537.36"
        s.headers["User-Agent"] = user_agent
        r=s.get(url)
        if r.status_code==200:
            r.encoding = chardet.detect(r.content).get("encoding")
            return r.text
        return None

#if __name__=="__main__":
#    htmlDownLoad = HtmlDownLoader()
#    print(htmlDownLoad.download("http://www.baidu.com"))

