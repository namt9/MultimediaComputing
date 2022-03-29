from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(executable_path="./chromedriver.exe")
 
# Open Google Images in the browser
browser.get('https://images.google.com/')
 
# Finding the search box
box = browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')

# Type the search query in the search box
query = "dogs"
box.send_keys(query)
box.send_keys(Keys.ENTER)
 
for i in range(1, 50):
   
    try:
        img = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        img.screenshot('C:\\Crawl\\img_crawled\\' + query + ' (' + str(i) + ').png')
        sleep(1)
    except:
        continue


browser.close()