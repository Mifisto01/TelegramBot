import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()

auth_html = s.get('https://smartprogress.do/')
auth_bs = BS(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']

print(csrf)

playload = {
    'YII_CSRF_TOKEN': csrf,
    'returnUrl': '/',
    'UserLoginForm[email]': 'priler96@gmai.com',
    'UserLoginForm[passqord]': 'tester123',
    'UserLoginForm[rememberMe]': 1
    }

answ = s.post('https://smartprogress/do/user/login/', data = playload)
answ_bs = BS(answ.content, 'html.pasrser')

print( 'Имя: {}\nУровень: {}\nОпыт: {}'.format(
    answ_bs.select('.yser-menu_name')[0].text.strip(),
    answ_bs.select('.yser-menu_info-text--lvl')[0].text.strip(),
    answ_bs.select('.yser-menu_info-text--exp')[0].text.strip()
    ))
