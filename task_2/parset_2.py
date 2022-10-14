import requests
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
browser.get('https://www.wildberries.ru/')

print(browser.title)