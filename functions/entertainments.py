from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def GetEntertainments(city):
    driver = webdriver.Chrome()
    # driver.set_window_position(-10000,0)
    driver.get("https://passport.yandex.ru/auth/list?origin=afisha&retpath=https%3A%2F%2Fafisha.yandex.ru%2Fmoscow")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/span/input").send_keys("aldaserastontoev@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[2]/div[1]/span/input").send_keys("twinkp0chta")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/div[1]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/header/div/div/div[1]/div[3]/button").click()
    # /html/body/div[6]/span/div[2]/div/div/div[1]/div[2]/span/span/input\ - new
    # /html/body/div[5]/span/div/div/div/div[1]/div[2]/span/span/input - old
    # SearchInputComponent
    # /html/body/div[6]/span/div/div/div/div[2]/div[1]/a
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[6]/span/div/div/div/div[1]/div[2]/span/span/input").send_keys(city)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[6]/span/div/div/div/div[2]/div[1]/a').click()
    time.sleep(2)
    # /html/body/div[2]/div[3]/div/div[2]/main/div/div[2]/div/div/div[1]/div/a/div
    # /html/body/div[2]/div[3]/div/div[1]/div/div/div[1]/div/div/a/h1
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/div/div/div[1]/div/div/a/h1').click()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    sob = soup.find_all('h2', class_='Title-fq4hbj-3 kkgEyg')
    dt = soup.find_all('li', class_='DetailsItem-fq4hbj-1 DqObr')

    sob_lst = [i.text for i in sob]
    dt_lst = [i.text for i in dt]
    lst_name = [i for i in dt_lst if dt_lst.index(i) % 2 != 0]
    lst_time = [i for i in dt_lst if dt_lst.index(i) % 2 == 0]
    result = []
    for i in range(len(lst_time)):
        result.append([lst_name[i], lst_time[i], sob_lst[i]])
    return result