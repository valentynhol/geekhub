import datetime

import scrapy
from bs4 import BeautifulSoup

from ..items import NewsScraperItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    date = None
    more_links = {}

    def __init__(self):
        self.item = NewsScraperItem()

    def start_requests(self):
        # First page request
        while True:
            try:
                year, month, day = input('Введіть дату у форматі YYYY/MM/DD.\n\t').split('/')
                input_date = datetime.date(int(year), int(month), int(day))

            except ValueError:
                continue
            result = self.verify_date(input_date)
            if result:
                break
            print('Неправильна дата')
        self.date = input_date.year, input_date.month, input_date.day
        url = f'http://vikka.ua/{year}/{month}/{day}'
        yield scrapy.Request(url, self.parse, errback=self.error)

    def verify_date(self, date):
        if date <= datetime.date.today():
            return True
        else:
            return False

    def __item_writer(self, soup):
        year, month, day = self.date
        self.item['date'] = f'date_{year}_{month}_{day}'

        tags = soup.select('.post-tag')
        tags_db = ''
        for tag in tags:
            if not tags_db:
                tags_db += '#' + tag.text
            else:
                tags_db += ', #' + tag.text

        self.item['news'] = {
            'title': soup.select_one('.post-title').text.strip(),
            'text': soup.select_one('.entry-content').text.strip(),
            'tags': tags_db,
            'link': self.more_links[soup.select_one('.post-title').text],
        }

    def error(self, error):
        print('\n\t\t_____________________________________________\n\t\t'
              '|||||||||||||||||||||||||||||||||||||||||||||\n\t\t'
              '---------------------------------------------\n\t\t'
              '|||||||||||||||||||||||||||||||||||||||||||||\n\t\t'
              '<<<<<=========| ПОСТІВ НЕМАЄ! |=========>>>>>\n\t\t'
              '|||||||||||||||||||||||||||||||||||||||||||||\n\t\t'
              '---------------------------------------------\n\t\t'
              '|||||||||||||||||||||||||||||||||||||||||||||\n\t\t'
              '_____________________________________________\n')

    def parse_more(self, response):
        self.item['counter'] += 1

        """
        This method scrapes and parses page with "more" page link
        """

        soup = BeautifulSoup(response.text, 'lxml')
        self.__item_writer(soup)
        yield self.item

    def parse(self, response):
        self.item['counter'] = 0
        soup = BeautifulSoup(response.text, 'lxml')

        # Gets "more" links and making request to every page
        news_links = soup.select('.more-link-style')
        news_titles = soup.select('.title-cat-post')

        for idx in range(len(news_links)):
            self.more_links[news_titles[idx].text] = news_links[idx]['href']
            yield scrapy.Request(news_links[idx]['href'], self.parse_more)

        if soup.select_one('.next'):
            yield scrapy.Request(soup.select_one('.next')['href'], self.parse)
