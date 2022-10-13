import requests
import random
from coloratura import cprint, Pantone
import os
os.system('color')

#choose .txt file containing good proxies
with open('all_proxies.txt') as f:
    proxy_list = f.read().splitlines()
print(proxy_list)

#choose .txt file with comments
with open('comments_21lo.txt', encoding='utf-8') as f:
    comments = f.read().splitlines()


proxy_test = '54.93.165.96:39593'
url = 'https://waszaedukacja.pl/ajax/opinia'

def create_data_21lo(text):
    data_21lo = {
    'id': 194,
    'plik': 'strony/ponadgimnazjalne/xxi-liceum-im-hugona-kollataja-warszawa-194.html',
    'co': 'placowka_dodaj',
    'ocena': 1,
    'rodzic': 0,
    'poziom': 0,
    'user': 'Gość.',
    'komentarz': text
    }
    return data_21lo

def create_data_tech(text):
    data_tech = {
    'id': 357,
    'plik': 'strony/ponadgimnazjalne/technikum-gastronomiczno-hotelarskie-nr-1-warszawa-357.html',
    'co': 'placowka_dodaj',
    'ocena': 1,
    'rodzic': 0,
    'poziom': 0,
    'user': 'Gość.',
    'komentarz': text
    }
    return data_tech

def random_comment():
    n = random.randint(0, len(comments)-1)
    return comments[n]

spam_counter = 0
def spam(proxy):
    comment = random_comment()
    print(comment)
    data = create_data_tech(comment)
    try:
        response = requests.post(url, data=data, proxies = {'http': proxy, 'https': proxy}, timeout = 3)
        if response.text == '<h5>Błąd. Zbyt wiele opinii w krótkim czasie z tego IP</h5>':
            proxy_list.remove(proxy)
        else:
            global spam_counter
            spam_counter+=1
        print(response.text)
        print('/n')
    except:
        proxy_list.remove(proxy)
        print(f'Błąd proxy - {proxy}')
        print('/n')

i=1
while len(proxy_list) > 0:
    print(f'///////////////////////////////////////////////////**{i}**///////////////////////////////////////////////////////////')
    print(len(proxy_list))

    for proxy in proxy_list:
        spam(proxy)
    i+=1

cprint(f'~~~~~~ You managed to spam {spam_counter} comments! ~~~~~~', color=Pantone.TURQUOISE)

end = input('Press enter to close: ')
#response = requests.post(url, data=data_tech, proxies = {'http': proxy, 'https': proxy}, timeout = 3)

#print(response.text)
#print(response)