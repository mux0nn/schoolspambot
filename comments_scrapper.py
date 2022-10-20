from selenium import webdriver
import time

file = open('txt/comments_21lo.txt', 'w', encoding = 'utf-8')

url_21lo = 'https://waszaedukacja.pl/ponadgimnazjalne/xxi-liceum-im-hugona-kollataja-warszawa-194'
url_tech = 'https://waszaedukacja.pl/ponadgimnazjalne/technikum-gastronomiczno-hotelarskie-nr-1-warszawa-357'

window = webdriver.Chrome('P:\Aplikacje\chromedriver\chromedriver.exe')
window.get(url_21lo)
window.implicitly_wait(10)

window.find_element_by_id('cooki_zamknij').click()
time.sleep(1)
window.find_element_by_id('wszystkie_opinie').click()
time.sleep(1)


comments = []
nr = 1
#find all comments on page
for comment in window.find_elements_by_class_name('komentarz'):
    print(f'{nr}. {comment.text}')
    comments.append(comment.text)
    nr+=1

#sort comments from oldest to newest
comments.reverse()

for comment in comments:
    try:
        file.write(f'{comment}\n')
    except:
        pass

window.close()

