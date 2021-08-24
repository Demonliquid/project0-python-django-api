# %%
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re



# %%
print('Crawling data and creating objects in database')
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





# %%
print('Crawling data and creating objects in database')
req = Request('https://coinranking.com/?sortby=asc&sorton=market-cap', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
bs = BeautifulSoup(html, 'html.parser')
rows = bs.find("tbody", class_="table__body").find_all('tr', class_="table__row")[0:5]
for row in rows:
    change = row.find('div', class_="change").get_text().strip().replace('\n', '')
    print({'change': change,
            })


# %%
re.sub('[^0-9]', '', yourString)

# %%
.get_text().strip().replace('\n', '').replace(' ', '').replace(',', '')



# %% BASE
print('Crawling data and creating objects in database')
req = Request('https://coinranking.com', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
bs = BeautifulSoup(html, 'html.parser')
rows = bs.find("tbody", class_="table__body").find_all('tr', class_="table__row")[0:5]
for row in rows:
    cryptocurrency_name = row.find('a', class_='profile__link').get_text().strip().replace('\n', '')
    cryptocurrency_subtitle = row.find('span', class_='profile__subtitle').get_text().strip().replace('\n', '')
    values = row.find_all('div', class_="valuta")
    price = values[0].get_text().strip().replace('\n','')
    market_cap = values[1].get_text().strip().replace('\n', '')
    change = row.find('div', class_="change").find('span').get_text().strip().replace('\n', '')
    print({'cryptocurrency_name':cryptocurrency_name,
            'cryptocurrency_subtitle': cryptocurrency_subtitle,
            'price': price,
            'market_cap':market_cap,
            'change':change})
