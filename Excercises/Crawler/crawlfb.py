from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd

browser = webdriver.Chrome(executable_path="./chromedriver.exe")

browser.get("https://www.facebook.com/ConfessionUIT/posts/pfbid0KNv5XJq5YsW6xdYySBUtrebsAp2uY5ujYFmgirwRVS9QBCqUfJVFt69A2gDPSQi9l")
sleep(10)

btcmt = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span/a')
btcmt.click()
sleep(5)

choseshow = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div')
choseshow.click()
sleep(5)

showall = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]')
showall.click()
sleep(10)

viewall = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]')
viewall.click()
sleep(5)

cmtlist = browser.find_elements_by_xpath("//div[@aria-label='Comment']")
sleep(5)

pt = []
ct = []
for cmt in cmtlist:
    poster = cmt.find_element_by_class_name('_6qw4')
    content = cmt.find_element_by_class_name('_3l3x')
    pt.append(poster.text)
    ct.append(content.text)

d = {'Poster': pt, 'Content': ct}
df = pd.DataFrame(data=d)
pd.DataFrame.to_csv(df, 'C:\Crawl\CrawlCmt2.csv')

browser.close()