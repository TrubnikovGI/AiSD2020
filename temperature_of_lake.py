Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get('https://pogoda1.ru/katalog/sverdlovsk-oblast/temperatura-vody/')
>>> soup = BeautifulSoup(r.content)
>>> m = []
>>> for table in soup.select('.x-table > .x-row'):
	m.append([])
	temperature_of_lake = table.select_one('.x-cell-water-temp').get_text(strip = True)
	link = [c for c in table.select('.x-cell > .link')]
	lake = link[0].text
	m[-1].append(temperature_of_lake)
	m[-1].append(lake)
	print(m[-1])

['+4.7', 'река Тура']
['+4.6', 'река Уфа']
['+4.1', 'река Чусовая']
['+3.7', 'река Исеть']
['+3.6', 'река Лозьва']
['+3.5', 'река Тавда']
['+3.3', 'река Пелым']
['+3.0', 'река Сосьва']
['+2.7', 'река Сылва']
['+1.2', 'река Пышма']
['+1.2', 'река Косьва']
['+4.9', 'река Бисерть']
['+4.5', 'река Ирбит']
['+2.2', 'река Каква ()']
['+0.8', 'река Турья']
['+0.6', 'река Вогулка']
['+2.6', 'река Сулём']
>>> 
