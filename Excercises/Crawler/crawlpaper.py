from pdb import post_mortem
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os

os.system('cls')

browser = webdriver.Chrome(executable_path='./chromedriver.exe')

browser.get('https://vnexpress.net/hung-dung-viet-nam-tran-trong-tung-tran-o-vong-loai-world-cup-4442124.html')
sleep(5)

title = browser.find_element_by_xpath('/html/body/section[3]/div/div[2]/h1')
sleep(5)

s1 = browser.find_element_by_xpath('/html/body/section[3]/div/div[2]/p')
sleep(5)

s = browser.find_elements_by_class_name('Normal')
sleep(5)
content = str(s1.text)
for i in s:
    content += str(i.text) + ' '
    
btn_more = browser.find_element_by_xpath('/html/body/section[4]/div/div[1]/div[2]/div/div/div[8]/a')
btn_more.click()
sleep(5)

c = []
cmt = browser.find_elements_by_class_name('full_content')
sleep(5)
for i in cmt:
    c.append(str(i.text))

poster = []
comment = []
for i in c:
    index = i.find('\n')
    poster.append(i[:index])
    comment.append(i[index+1:])

d = {}
for i in range(len(comment)):
    d[poster[i]] = comment[i]


items = list(d.items())
dic2lst = []
for i in range(len(items)):
    print(items[i], '\n\n')
    temp = items[i]
    dic2lst.append(temp)

paper = {'title': [title.text],
        'content': [content],
        'poster/comment': [dic2lst]}

df = pd.DataFrame(data=paper)
pd.DataFrame.to_csv(df, 'C:\Crawl\data.csv')

browser.close()



