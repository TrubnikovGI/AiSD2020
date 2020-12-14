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
>>> 
