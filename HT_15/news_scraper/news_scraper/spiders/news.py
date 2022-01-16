import datetime
import csv

import scrapy
from bs4 import BeautifulSoup


class NewsSpider(scrapy.Spider):
    name = 'news'
    date = None
    more_links = []
    more_link_counter = 0

    def get_date(self):
        """
        This method checks and sets the value of the entered date into self.date
        """

        # Infinite cycle for date verification
        while True:
            input_date = input('Введіть дату у форматі YYYY/MM/DD.\n\t').split('/')

            # Check length of each date element
            if len(input_date) == 3 and len(input_date[0]) == 4 and len(input_date[1]) == 2 and len(input_date[2]) == 2:
                try:
                    year = int(input_date[0])
                    month = int(input_date[1])
                    day = int(input_date[2])
                except ValueError:
                    print('Введіть дату у правильному форматі!!!')
                    continue

                # Check if a date is possible
                if datetime.date.today().year > year > 2009:
                    if 12 >= month >= 1:
                        if month in [1, 3, 5, 7, 8, 10, 12]:
                            if 31 >= day >= 1:
                                break
                            else:
                                print('Введіть дату у правильному форматі!!!')
                                continue
                        elif month == 2:
                            if year % 4 == 0 and not year % 100 == 0:
                                if 29 >= day >= 1:
                                    break
                                else:
                                    print('Введіть дату у правильному форматі!!!')
                                    continue
                            else:
                                if 28 >= day >= 1:
                                    break
                                else:
                                    print('Введіть дату у правильному форматі!!!')
                                    continue
                        else:
                            if 30 >= day >= 1:
                                break
                            else:
                                print('Введіть дату у правильному форматі!!!')
                                continue
                    else:
                        print('Введіть дату у правильному форматі!!!')
                        continue

                elif year == 2009:
                    if month == 9:
                        if day >= 21:
                            break
                        else:
                            print('Введіть дату більшу, ніж 2009/09/21.')
                            continue
                    elif month > 9:
                        break
                    else:
                        print('Введіть дату більшу, ніж 2009/09/21.')
                        continue

                elif year == datetime.date.today().year:
                    if month == datetime.date.today().month:
                        if day <= datetime.date.today().day:
                            break
                        else:
                            print('Введіть дату більшу, ніж 2009/09/21.')
                            continue
                    elif month < datetime.date.today().month:
                        break
                    else:
                        print('На жаль, в майбутнє я не маю доступу.')
                        continue

                else:
                    print(f'Введіть дату, не меншу, ніж 2009/09/21 і не більшу, '
                          f'ніж сьогоднішня дата({datetime.date.today().strftime("%Y/%m/%d")})!!!')
                    continue
            else:
                print('Введіть дату у правильному форматі!!!')
                continue

        # If verification completed, breaks out of the cycle and sets self.date
        self.date = input_date

    def start_requests(self):
        # First page request
        self.get_date()
        year, month, day = self.date
        url = f'http://vikka.ua/{year}/{month}/{day}'
        yield scrapy.Request(url, self.parse)

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
        year, month, day = self.date
        with open(f'{year}_{month}_{day}.csv', 'a') as news_csv:
            news_csv.truncate(0)
            csv_writer = csv.DictWriter(news_csv, delimiter=',',
                                        fieldnames=['title', 'text', 'tags', 'link'])
            csv_writer.writeheader()

        soup = BeautifulSoup(response.text, 'lxml')

        # Gets "more" links and making request to every page
        news_links = soup.select('.more-link-style')

        for news_link in news_links:
            self.more_links.append(news_link['href'])
            yield scrapy.Request(news_link['href'], self.parse_more)
