import re
from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from .models import Cryptocurrency, Dolarhoy


@shared_task

def crawl_currency():
    print('Crawling cryptos')
    req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find("tbody", class_="table__body").find_all('tr', class_="table__row")[0:5]
    for row in rows:
        cryptocurrency_name = row.find('a', class_='profile__link').get_text().strip().replace('\n', '').capitalize()
        cryptocurrency_subtitle = row.find('span', class_='profile__subtitle').get_text().strip().replace('\n', '').upper()
        values = row.find_all('div', class_="valuta")
        price = values[0].get_text().strip().replace('\n', '').replace(' ', '').replace(',', '').replace('$', '')
        market_number = values[1].get_text().strip().replace('\n', '').replace('$', '').lstrip()
        market_number = re.sub('[^0-9.]', '', market_number)
        market_unit = values[1].get_text().strip().replace('\n', '').replace('$', '').lstrip()
        market_unit = re.sub('[^a-z]', '', market_unit)
        change = row.find('div', class_="change").get_text().strip().replace('\n', '')
        print({'cryptocurrency_name':cryptocurrency_name,
               'cryptocurrency_subtitle': cryptocurrency_subtitle,
               'price': price,
               'market_number':market_number,
               'market_unit':market_unit,
               'change':change})
        Cryptocurrency.objects.create(
                                    cryptocurrency_name=cryptocurrency_name,
                                    cryptocurrency_subtitle=cryptocurrency_subtitle,
                                    price=price,
                                    market_number=market_number,
                                    market_unit=market_unit,
                                    change=change
                                    )
        sleep(3)


def update_currency():
    print('Updating cryptos')
    req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find("tbody", class_="table__body").find_all('tr', class_="table__row")[0:5]
    for row in rows:
        cryptocurrency_name = row.find('a', class_='profile__link').get_text().strip().replace('\n', '').capitalize()
        cryptocurrency_subtitle = row.find('span', class_='profile__subtitle').get_text().strip().replace('\n', '').upper()
        values = row.find_all('div', class_="valuta")
        price = values[0].get_text().strip().replace('\n', '').replace(' ', '').replace(',', '').replace('$', '')
        market_number = values[1].get_text().strip().replace('\n', '').replace('$', '').lstrip()
        market_number = re.sub('[^0-9.]', '', market_number)
        market_unit = values[1].get_text().strip().replace('\n', '').replace('$', '').lstrip()
        market_unit = re.sub('[^a-z]', '', market_unit)
        change = row.find('div', class_="change").get_text().strip().replace('\n', '')
        data = {'cryptocurrency_name': cryptocurrency_name,
                'cryptocurrency_subtitle': cryptocurrency_subtitle,
                'price': price,
                'market_number':market_number,
                'market_unit':market_unit,
                'change':change}
        print({'cryptocurrency_name': cryptocurrency_name,
               'cryptocurrency_subtitle': cryptocurrency_subtitle,
               'price': price,
               'market_number':market_number,
               'market_unit':market_unit,
               'change': change})
        Cryptocurrency.objects.filter(cryptocurrency_name=cryptocurrency_name).update(**data)
        sleep(3)


def crawl_dolar():
    print('Crawling dollars')
    req = Request('https://dolarhoy.com/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find("div", class_="tile is-parent is-7 is-vertical").find_all('div', class_="tile is-child")[0:5]
    for row in rows:
        tipo_dolar = row.find('a', class_='title').get_text().strip().replace('\n', '').capitalize()
        values = row.find_all('div', class_="venta")
        cotizacion_en_pesos = values[0].get_text().strip().replace('\n', '').replace(' ', '').replace(',', '').replace('$', '')
        cotizacion_en_pesos = re.sub('[^0-9.]', '', cotizacion_en_pesos)
        print({'tipo_dolar':tipo_dolar,
            'cotizacion_en_pesos': cotizacion_en_pesos})
        Dolarhoy.objects.create(
                                tipo_dolar=tipo_dolar,
                                cotizacion_en_pesos=cotizacion_en_pesos
                                )
        sleep(3)


def update_dolar():
    print('Updating data')
    req = Request('https://dolarhoy.com/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    rows = bs.find("div", class_="tile is-parent is-7 is-vertical").find_all('div', class_="tile is-child")[0:5]
    for row in rows:
        tipo_dolar = row.find('a', class_='title').get_text().strip().replace('\n', '').capitalize()
        values = row.find_all('div', class_="venta")
        cotizacion_en_pesos = values[0].get_text().strip().replace('\n', '').replace(' ', '').replace(',', '').replace('$', '')
        cotizacion_en_pesos = re.sub('[^0-9.]', '', cotizacion_en_pesos)
        data = {'tipo_dolar': tipo_dolar,
                'cotizacion_en_pesos': cotizacion_en_pesos}
        print({'tipo_dolar': tipo_dolar,
                'cotizacion_en_pesos': cotizacion_en_pesos})
        Dolarhoy.objects.filter(tipo_dolar=tipo_dolar).update(**data)
        sleep(3)




crawl_currency()
crawl_dolar()

while True:
    update_currency()
    update_dolar()
    sleep(15)