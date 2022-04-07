from selenium import webdriver
from time import  sleep
from pandas import DataFrame
import csv

titles = []
abstracts = []

# Khai báo biến browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# Mở 1 trang web
browser.get("https://ieeexplore.ieee.org/author/37268947300")

# Click nút accept cookie của trang
accept = browser.find_element_by_xpath("/html/body/div[1]/div")
accept.click()

sleep(10)

#Cho chạy trong 20 pages
for page in range(20):
    #Lấy links của tất cả bài báo trong trang
    doc_links = browser.find_elements_by_css_selector(".text-md-md-lh a")
    #Duyệt từng bài báo
    for i in range(len(doc_links)):
        print(i)
        #Mở trang bài báo
        doc_links[i].click()

        sleep(10)

        #Lấy dữ liệu về title và abstract của bài báo
        title = browser.find_element_by_css_selector(".text-2xl-md-lh span")
        abstract = browser.find_element_by_css_selector(".abstract-text .u-mb-1 div")

        titles.append(title.text)
        abstracts.append(abstract.text)

        print("Title:", title.text)
        print("Abstract:", abstract.text)

        sleep(5)

        #Quay trở lại trang trước
        browser.back()

        sleep(10)

        #Lấy lại links của tất cả bài báo vì khi quay lại links các bài báo sẽ bị thay đổi, các links bài báo thu thập trước không thể sử dụng lại
        doc_links = browser.find_elements_by_css_selector(".text-md-md-lh a")

        #Khi thu thập hết thì chuyển page
        if (i == (len(doc_links) - 1)):
            next_page = browser.find_element_by_css_selector(".stats-Pagination_arrow_next_2")
            next_page.click()

#Trích xuất dữ liệu ra file csv
raw_data = {'Title': titles,
            "Abstract": abstracts}
df = DataFrame(raw_data, columns=["Title", "Abstract"])
df.to_csv('data.csv')
print(df)

