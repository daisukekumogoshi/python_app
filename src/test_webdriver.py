from selenium import webdriver
import pandas

driver = webdriver.Chrome("../selenium/chromedriver")
driver.get("https://sports.yahoo.co.jp/news/list?id=ws")
driver.close()