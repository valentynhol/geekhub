import datetime
import csv

import scrapy
from bs4 import BeautifulSoup


class NewsSpider(scrapy.Spider):
    name = 'news'
    date = None
    more_links = []
    more_link_counter = 0

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
        yield scrapy.Request(url, self.parse)

    def verify_date(self, date):
        if datetime.date(2009, 9, 21) <= date <= datetime.date.today():
            return True
        else:
            return False

    def __csv_writer(self, soup):
        year, month, day = self.date

        tags = soup.select('.post-tag')
        tags_csv = ''
        for tag in tags:
            if not tags_csv:
                tags_csv += '#' + tag.text
            else:
                tags_csv += ', #' + tag.text

        with open(f'{year}_{month}_{day}.csv', 'a') as news_csv:
            csv_writer = csv.DictWriter(news_csv, delimiter=',',
                                        fieldnames=['title', 'text', 'tags', 'link'])
            csv_writer.writerow({
                'title': soup.select_one('.post-title').text.strip(),
                'text': soup.select_one('.entry-content').text.strip(),
                'tags': tags_csv,
                'link': self.more_links[self.more_link_counter-1],
            })

    def parse_more(self, response):
        """
        This method scrapes and parses page with "more" page link
        """
        self.more_link_counter += 1
        soup = BeautifulSoup(response.text, 'lxml')

        self.__csv_writer(soup)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        year, month, day = self.date
        with open(f'{year}_{month}_{day}.csv', 'a') as news_csv:
            news_csv.truncate(0)
            csv_writer = csv.DictWriter(news_csv, delimiter=',',
                                        fieldnames=['title', 'text', 'tags', 'link'])
            csv_writer.writeheader()

        # Gets "more" links and making request to every page
        news_links = soup.select('.more-link-style')

        for news_link in news_links:
            self.more_links.append(news_link['href'])
            yield scrapy.Request(news_link['href'], self.parse_more)
