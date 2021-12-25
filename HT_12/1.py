import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
import os

os.remove('quotes.db')

with open('quotes.csv', 'a') as quotes_csv:
    quotes_csv.truncate(0)
    csv_writer = csv.DictWriter(quotes_csv, delimiter=',', fieldnames=['Quote',
                                                                       'Author',
                                                                       'Author Born Date',
                                                                       'Author Born Location',
                                                                       'Author Description'])

    csv_writer.writeheader()

quotes_db = sqlite3.connect('quotes.db')
cur = quotes_db.cursor()

cur.execute('''DROP TABLE IF EXISTS quotes''')

quotes_db.commit()
quotes_db.close()

next_link_bool = True
next_link = ''

while True:
    page = requests.get('http://quotes.toscrape.com'+next_link).text

    soup = BeautifulSoup(page, 'lxml')
    quotes = soup.select('.quote')
    for quote in quotes:
        quote_text = quote.select_one('.text').text
        quote_author = quote.select_one('.author').text
        author_info_link = quote.select_one('a')['href']

        author_info = requests.get('http://quotes.toscrape.com'+author_info_link).text
        author_soup = BeautifulSoup(author_info, 'lxml')

        author_born_date = author_soup.select_one('.author-born-date').text
        author_born_location = author_soup.select_one('.author-born-location').text
        author_description = author_soup.select_one('.author-description').text

        with open('quotes.csv', 'a') as quotes_csv:
            csv_writer = csv.DictWriter(quotes_csv, delimiter=',', fieldnames=['Quote',
                                                                               'Author',
                                                                               'Author Born Date',
                                                                               'Author Born Location',
                                                                               'Author Description'])

            csv_writer.writerow({'Quote': quote_text, 'Author': quote_author, 'Author Born Date': author_born_date,
                                 'Author Born Location': author_born_location, 'Author Description': author_description})

        quotes_db = sqlite3.connect('quotes.db')
        cur = quotes_db.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS quotes(
                    quote TEXT NOT NULL,
                    author TEXT NOT NULL,
                    author_born_date TEXT NOT NULL,
                    author_born_location TEXT NOT NULL,
                    author_description TEXT NOT NULL)''')

        cur.execute('''INSERT INTO quotes VALUES (?, ?, ?, ?, ?)''',
                    (quote_text, quote_author, author_born_date, author_born_location, author_description))

        quotes_db.commit()
        quotes_db.close()

    next_link_bool = bool(soup.select_one('.next'))
    try:
        next_link = soup.select_one('.next > a')['href']
    except TypeError:
        break
