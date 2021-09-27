chrome_driver = "C:/Users/91892/PycharmProjects/selerium_driver/chromedriver.exe"
import time
import lxml
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wb
import requests

URL_Form = "https://docs.google.com/forms/d/e/1FAIpQLSd9U9egdWrILNNqmDnXASSODTITQBj5wfKDdU-lBSGgIAAt3g/viewform?usp=sf_link"
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.82565026437128%2C%22east%22%3A-122.04100773562872%2C%22south%22%3A37.499747559280394%2C%22north%22%3A38.0498122007862%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A411731%2C%22max%22%3A1152845%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A2800%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
header = {
'http://myhttpheader.com/'
# get your link to find your computer https protocol
}

def google_form(price,link,addr):
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addr)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(2)
    return


response = requests.get(url=URL,headers=header)
time.sleep(3)
html_text = response.text
soup = bs(html_text,'lxml')
# values = soup.select('ul',class_='photo-cards photo-cards_wow photo-cards_short')

driver = wb.Chrome(chrome_driver)
driver.maximize_window()
driver.get(url=URL_Form)
time.sleep(2)


for i in soup.findAll('li'):
    x=i.find('a',class_='list-card-link list-card-link-top-margin list-card-img')
    price = i.find('div',class_='list-card-price')

    if x!=None:
        price = (price.text)
        address = x.find('img')['alt']
        x =x['href']
        if x[0:5]!="https":
                         x = f"https://www.zillow.com{x}"

        google_form(price,x,address)

driver.quit()