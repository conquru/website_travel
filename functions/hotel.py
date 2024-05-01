from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def GetHotel(end):
    driver = webdriver.Chrome()
    driver.get('https://sletat.ru/hotels/russia/')

    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div/div[1]/div[1]').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div').click()
    driver.find_element(By.TAG_NAME, 'input').send_keys(end)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div/div[2]/div/a').click()
    time.sleep(15)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    name = soup.find_all('h3',class_='Map__HotelName__title')
    hotelprice = soup.find_all('span', class_='sc-guJBdh gFaGLE')
    name_lst = [i.text for i in name]
    hotelprice_lst = [i.text for i in hotelprice]
    result = []

    for i in range(len(hotelprice_lst)):
        result.append([name_lst[i], hotelprice_lst[i]])
    return result