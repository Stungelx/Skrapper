# включення необхідних бібліотек
import bs4
import requests

# Створення перемінної з данними сайту
website = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
site_cod = requests.get(website)
site_cod.raise_for_status()
clear_cod = bs4.BeautifulSoup(site_cod.text, 'html.parser')

# Визначення кількості сторінок
cloud=[]
numbers_of_pages = clear_cod.find_all('a', class_ ='page-link')
for number in numbers_of_pages:
    try:
        cloud.append(int(number.text))
    except ValueError:
        pass

# Цикл перебору сторінок
for i in range(1, max(cloud)+1):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}"

    # Створення перемінної з данними сайту
    site_cod = requests.get(url)
    site_cod.raise_for_status()
    clear_cod = bs4.BeautifulSoup(site_cod.text, 'html.parser')

    # Знайти всі обєкти на сторінці
    mashines = clear_cod.find_all('div', class_ ='col-md-4 col-xl-4 col-lg-4')
    #Знайти необхідні дані цих обєктів
    for mashine in mashines:
        name1 = mashine.find('a', class_='title')
        description = mashine.find('p', class_ = 'description card-text')
    # Вивести ці дані
        print(name1.text,"\n", description.text)