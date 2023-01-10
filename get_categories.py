import json

import requests
from bs4 import BeautifulSoup

headers = headers

params = {
    'reff': 'menu_main',
}

response = requests.get('https://www.mvideo.ru/komputernye-komplektuushhie-5427', params=params, headers=headers)
try:
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find('ul', class_='accessories-product-list').find_all('li')
    categories_dict = {}
    for category in categories:
        category_name = category.find('div', class_='fl-category__title').text
        category_id = category.find('a').get('href').split('-')[-1]
        categories_dict[category_name] = category_id
    with open('categories_dict.json', 'w') as file:
        json.dump(categories_dict, file, indent=4, ensure_ascii=False)
    print('[+] Получение категорий завершилось успешно')
except:
    print(f'[error] Ошибка получения категорий')
