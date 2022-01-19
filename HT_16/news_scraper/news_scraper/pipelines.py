
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class NewsScraperPipeline:
    def __init__(self):
        self.database = sqlite3.connect('news.db')
        self.cur = self.database.cursor()

    def process_item(self, item, spider):
        if item['counter'] == 1:
            self.cur.execute(f'''DROP TABLE IF EXISTS {item['date']}''')
            self.cur.execute(f'''CREATE TABLE {item['date']}(
                                        title TEXT,
                                        content TEXT,
                                        tags TEXT,
                                        link TEXT)''')

        self.cur.execute(f'''INSERT INTO {item['date']} VALUES (?,?,?,?)''', (item['news']['title'],
                                                                              item['news']['text'],
                                                                              item['news']['tags'],
                                                                              item['news']['link']))
        self.database.commit()
        return item

    def close_spider(self, spider):
        self.database.close()
