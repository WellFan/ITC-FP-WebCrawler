from datetime import datetime
import requests
from lxml import etree
from time import sleep


class Crawler(object):
    def __init__(self,
                 base_url='https://www.csie.ntu.edu.tw/news/',
                 rel_url='news.php?class=101'):
        self.base_url = base_url
        self.rel_url = rel_url

    def crawl(self, start_date, end_date,
              date_thres=datetime(2012, 1, 1)):
        """Main crawl API

        1. Note that you need to sleep 0.1 seconds for any request.
        2. It is welcome to modify TA's template.
        """
        if end_date < date_thres:
            end_date = date_thres
        contents = list()
        page_num = 0
        while True:
            rets, last_date = self.crawl_page(
                start_date, end_date, page=f'&no={page_num}')
            page_num += 10
            if rets:
                contents += rets
            if last_date < start_date:
                break
        return contents

    def crawl_page(self, start_date, end_date, page=''):
        res = requests.get(
            self.base_url + self.rel_url + page,
            headers={'Accept-Language':
                     'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6'}
        ).content.decode()
        sleep(0.1)
        parser = etree.HTML(res)
        xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/table/tbody'
        root = parser.xpath(xpath)
        dates = root[0].xpath('//tr/td[1]/text()')
        titles = root[0].xpath('//tr/td[2]/a/text()')
        rel_urls = root[0].xpath('//tr/td[2]/a/@href')
        contents = list()
        for i, (date, title, rel_url) in enumerate (zip(dates, titles, rel_urls)):
            date = datetime.strptime(date, '%Y-%m-%d')
            if start_date <=date <= end_date:
                url = self.base_url + rel_url
                content = self.crawl_content(url)
                contents.append((date, title, content))
            if i + 1 == len(dates):
                last_date=date
        return contents, last_date

    def crawl_content(self, url):
        res = requests.get(url).content.decode()
        parser = etree.HTML(res)
        xpath = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]//text()'
        content=parser.xpath(xpath)
        return ' '.join(content)
        
        raise NotImplementedError