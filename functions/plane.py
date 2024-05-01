from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def GetTickets(start, end, time_data):
    driver = webdriver.Chrome()
    driver.get("https://www.tutu.ru/")
    driver.find_element(By.NAME, "city_from").send_keys(start)
    driver.find_element(By.NAME, "city_to").send_keys(end)
    driver.find_element(By.NAME, "date_from").send_keys(time_data)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "spinner").click()
    time.sleep(2)



    soup = BeautifulSoup(driver.page_source, "html.parser")
    alltc = soup.find_all('div', class_='_1EbfC9wDT-QCSBiXIT-Qwv _3fnckNAu9Q8NduBw930kvb')
    company = soup.find_all('span', class_='_19j5UevMdTcHGRMJLu4Wtd o-text-inline o-text-paragraphSmall')
    timeopen = soup.find_all('span', class_='UFlg3tcFvqtPw3IuhhhM3 o-text-inline o-text-headerMedium o-text-headerLarge-md')
    timereread = soup.find_all('span', class_='_3Cc6coU1wDRExPJuZGJ9R3 o-text-inline o-text-secondary o-text-paragraphSmall')
    timeclose = soup.find_all('span', class_='_15mC1UzJwjHpnQolp1FCYX o-text-inline o-text-headerMedium o-text-headerLarge-md')
    price = soup.find_all('span', class_= '_35oFq5jcD6iVmQcaiPZULW o-price-nowrap o-text-inline o-text-headerMedium o-text-headerLarge-md')
    rating = soup.find_all('span', class_='_1nQoa70TqdPlVGIIUWANp8 o-text-inline o-text-paragraphSmall')
    rating_lst = [i.text for i in rating]
    timeopen_lst = [i.text for i in timeopen]
    timereread_lst = [i.text for i in timereread]
    timeclose_lst = [i.text for i in timeclose]
    price_lst = [i.text for i in price]
    company_lst = [i.text for i in company]
    
    result = []
    for i in range(len(price_lst)):
        result.append([company_lst[i], rating_lst[i], timeopen_lst[i],timereread_lst[i] , timeclose_lst[i],  price_lst[i]])
    return result