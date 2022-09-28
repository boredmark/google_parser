from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time


def input_info():
    search_list = str(input('Print your google request, separated by a comma\n '
                            'Example: dog,cat,city tours\n'))
    req_list = search_list.split(',')
    return req_list


def research(req):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    d = {}
    for i in req:
        with webdriver.Chrome(executable_path='./driver/chromedriver', options=options_chrome) as browser:
            browser.get('http://www.google.com')
            time.sleep(2)
            cookie = browser.find_element(By.ID, 'W0wltc')
            cookie.click()
            time.sleep(2)
            search_line = browser.find_element(By.NAME, 'q')
            search_line.send_keys(i)
            time.sleep(2)
            search = browser.find_element(By.NAME, 'btnK')
            search.click()
            time.sleep(2)
            elements = browser.find_elements(By.CLASS_NAME, 'yuRUbf')
            links1 = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in elements]
            browser.find_element(By.XPATH, '//a[@aria-label="Page 2"]').click()
            time.sleep(2)
            elements = browser.find_elements(By.CLASS_NAME, 'yuRUbf')
            links2 = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in elements]
            browser.find_element(By.XPATH, '//a[@aria-label="Page 3"]').click()
            time.sleep(2)
            elements = browser.find_elements(By.CLASS_NAME, 'yuRUbf')
            links3 = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in elements]
            browser.find_element(By.XPATH, '//a[@aria-label="Page 4"]').click()
            time.sleep(2)
            elements = browser.find_elements(By.CLASS_NAME, 'yuRUbf')
            links4 = [i.find_element(By.TAG_NAME, 'a').get_attribute('href') for i in elements]
            res = links1 + links2 + links3 + links4
            time.sleep(2)
        d[i] = res[:30]
    return d


def create_csv(req):
    with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(req)


def fill_csv(d):
    with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        for i in range(30):
            x = [j[i] for j in d.values()]
            writer.writerow(x)


def main():
    info = input_info()
    result_of_research = research(info)
    create_csv(info)
    fill_csv(result_of_research)

main()


