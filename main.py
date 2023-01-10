import json
import math
import random
import time
import requests
from conf import headers
import os

headers = headers

session = requests.Session()


def get_pages(category_id):
    params = {
        'categoryId': category_id,
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }
    response = session.get('https://www.mvideo.ru/bff/products/listing', params=params, headers=headers)
    if response:
        total = response.json().get('body').get('total')
        pages = math.ceil(total / 24)
        return pages


def get_product_ids(category_id):
    for i in range(get_pages(category_id)):
        offset = f'{i * 24}'

        params = {
            'categoryId': category_id,
            'offset': offset,
            'limit': '24',
            'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            'doTranslit': 'true',
        }

        time.sleep(random.randrange(1, 3))
        response = session.get('https://www.mvideo.ru/bff/products/listing', params=params, headers=headers)
        products_ids = response.json().get('body').get('products')
        yield products_ids


def get_products_data(category_id):
    products_data = []
    for product_ids in get_product_ids(category_id):
        json_data = {
            'productIds': product_ids,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': True,
        }
        time.sleep(random.randrange(1, 3))
        response = requests.post('https://www.mvideo.ru/bff/product-details/list', headers=headers, json=json_data)
        products_data.append(response.json().get('body').get('products'))
    return products_data


def write_data(category_name, category_id):
    products_data = geet_products_data(category_id)
    if not os.path.exists('data'):
        os.mkdir('data')
    with open(f'data/{category_name}_{category_id}.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)
    print(f'[+] Категория {category_name}_{category_id} записана')


def main():
    with open('categories_dict.json') as file:
        categories_dict = json.load(file)
    for category in categories_dict:
        category_id = categories_dict[category]
        write_data(category, category_id)


if __name__ == '__main__':
    main()
