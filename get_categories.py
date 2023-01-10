import json

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427?reff=menu_main',
    'Connection': 'keep-alive',
    'Cookie': '__lhash_=ac7a49bb8a683982aeeebff65520f1ce; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; __js_p_=568,3600,0,1,0; __jhash_=988; __jua_=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%3B%20rv%3A103.0%29%20Gecko%2F20100101%20Firefox%2F103.0; flacktory=no; BIGipServeratg-ps-prod_tcp80=1208278026.20480.0000; bIPs=930512162; Old_Browser_Accept_the_Risk_and_Continue=1; MVID_GUEST_ID=22145447006; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=J0Tvj9CSd4JGN62zC4GDSnLShh5hL2HH43d013rpgTSQQ5s0glPy!1736622111; MVID_CALC_BONUS_RUBLES_PROFIT=true; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=true; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1208278026.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=tablet; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VDOxFjIVBsQndZZxhDHxNJfidmGy4hWWQtMy5zCR93X10id1VOfGdZSCMWRHAMTlt0fRVEGjxsIGVNWyFEVk5qJh8Yem4nVg0LXT5FdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0Jzeiw+aSVlSFwmTFpJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=4LJLSw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VDOxFjIVBsQndZZxhDHxNJfidmGy4hWWQtMy5zCR93X10id1VOfGdZSCMWRHAMTlt0fRVEGjxsIGVNWyFEVk5qJh8Yem4nVg0LXT5FdmUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0Jzeiw+aSVlSFwmTFpJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=4LJLSw==; cfidsgib-w-mvideo=WBplFXfcPjJ3S7R8YOkAqjgAuSgT+tdRuvdV/SKOOno3YlZj1kowhbZxwOzcyiWuK+c0thO/GGcq3PRJNmwrVfTP2TFtqrbAyn1grSk1lX2Wk3djJMjtUHPeY6FokMbInpgjrO2DcwIdoB961Uqt2E1dtrzndWEX2Zq6kA==; cfidsgib-w-mvideo=jb6C2mMvTQ8/BIxODdLq/9xlIhbl9OzNm9U6iHcPg6TPg2gmBUxberZQZgPRueVNNwTiALtHRR8NP1Za/YgAdO3+WBAvnv/ZivIbLv3lrRughkuj4n7zjY34IE2YXhLsWkQeJa0lEQPydzSgS3pWzv3+NEbCCiKxiKAXFQ==; cfidsgib-w-mvideo=jb6C2mMvTQ8/BIxODdLq/9xlIhbl9OzNm9U6iHcPg6TPg2gmBUxberZQZgPRueVNNwTiALtHRR8NP1Za/YgAdO3+WBAvnv/ZivIbLv3lrRughkuj4n7zjY34IE2YXhLsWkQeJa0lEQPydzSgS3pWzv3+NEbCCiKxiKAXFQ==; gsscgib-w-mvideo=6qRXWPIXacEPgSbASDyiuYXC18zicEY0a8pbZ5amiaroj/maAbwQUuPSHfe+3+W0JWYP+Bu70CtAt3wtmpQ9X6fHbLfbN3FGDSF4vXc17yzU72e3eNtm3pj246augbeimu1b8FYLI5qhi6is+/+jhYnw/c1ApJtBmUUc7fgyra5z/4p0sPBEqzLnNVs9qax5HV+HT4qng4IPJhB3cexVKjE5F53CB3fgTga/O5mlmFUZhba1vMfEGt0g9harow==; gsscgib-w-mvideo=6qRXWPIXacEPgSbASDyiuYXC18zicEY0a8pbZ5amiaroj/maAbwQUuPSHfe+3+W0JWYP+Bu70CtAt3wtmpQ9X6fHbLfbN3FGDSF4vXc17yzU72e3eNtm3pj246augbeimu1b8FYLI5qhi6is+/+jhYnw/c1ApJtBmUUc7fgyra5z/4p0sPBEqzLnNVs9qax5HV+HT4qng4IPJhB3cexVKjE5F53CB3fgTga/O5mlmFUZhba1vMfEGt0g9harow==; fgsscgib-w-mvideo=yVJW8dc2385467e969ca50aff0a28c4e814828cc; fgsscgib-w-mvideo=yVJW8dc2385467e969ca50aff0a28c4e814828cc; gssc218=; __hash_=4628e9fe984c567ca8428a0034dcc8d1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',

}

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
