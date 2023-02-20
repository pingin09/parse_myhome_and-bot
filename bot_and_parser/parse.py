import bs4
import requests
import urllib.parse
import re


class MyhomeParser:
    def __init__(self, params):
        self.params = params
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

    def get_page(self, page: int = None):
        temp_params = self.params.copy()
        if page and page > 1:
            temp_params = self.params.copy()
            temp_params['page'] = page
        url = 'https://www.myhome.ge/ru/s'
        r = self.session.get(url, params=temp_params)
        return r.text

    def get_pagination_limit(self):
        text = self.get_page()
        soup = bs4.BeautifulSoup(text, 'lxml')
        pages = soup.select('a.page-link')
        last_page = pages[-1]
        href = last_page.get('href')
        r = urllib.parse.urlparse(href)
        s = ''
        for i in r[2]:
            if i.isdigit():
                s += i
        return int(s)

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div.statement-card')
        all_block = []
        for item in container:
            block = self.parse_block(item=item)
            if block != None:
                all_block.append(block)

        return all_block

    def parse_block(self, item):
        try:
            url_block = item.select_one('a.card-container')
            href = url_block.get('href')
            url = href[0:37]
            title_block = item.select_one('h5.card-title')
            title = title_block.string.strip()
            price_block = item.select_one('b.item-price-gel')
            price_block2 = item.select_one('b.item-price-usd')
            priceL = price_block.string.strip() + ' GEL'
            priceD = price_block2.string.strip() + ' $'
            date_block = item.select_one('div.statement-date')
            date = date_block.string.strip()
            images = item.select_one('img.swiper-lazy')
            images = images.get('data-src')
            images1 = re.sub('thumbs', 'large', images)
            images2 = re.sub('1.jpg', '2.jpg', images1)
            images3 = re.sub('1.jpg', '3.jpg', images1)
            adress = item.select_one('.address')
            adress = adress.get("title")

            return {"title": title, "url": url, "priceL": priceL, "priceD": priceD, "date": date, "images1": images1,
                    "images2": images2, "images3": images3, 'adress': adress}

        except AttributeError:

            return None

    def parse_all(self):
        limit = self.get_pagination_limit()
        print(f'Всего страниц {limit}')
        block_all = []
        for i in range(1, limit + 1):
            block_all += self.get_blocks(page=i)
        value_str = len(block_all)
        temp2 = value_str % 5
        block_all_group = []
        if temp2 == 0:
            block_all_group = [block_all[i: i + 5] for i in range(0, value_str, 5)]
        elif temp2 != 0:
            block_all_group = [block_all[i: i + 5] for i in range(0, value_str, 5)]
        print(value_str)
        for i in block_all_group:
            print(i)
        return block_all_group
