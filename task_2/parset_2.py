import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path=r"C:\Users\vika0\Desktop\Папки\NFT\hashlips_nft_minting_dapp-1.0.1\node_modules\@babel\traverse\lib\path\to\chromedriver.exe")
browser.get('https://www.wildberries.ru/')

print(browser.title)

links = browser.find_element('a', By.TAG_NAME)

[print(link.text) for link in links]


time.sleep(60)
browser.close()