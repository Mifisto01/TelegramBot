import requests
from bs4 import BeautifulSoup as BS

page = 1

while True:
    r = requests.get('http://l2-top.ru/' + str(page)) #ссылка на сайт с которого нужно взять информацию
    html = BS(r.content, 'html.parser') #результат переводим в библиотеку БьюСуп
    items = html.select('.items > .article-summary') #

    if (len(items)): #Данный код выводит название игры с каждой страницы
        for el in items:
            title = el.select('.caption > a')
            print(title[0].text)
        page += 1
    else:
        break
