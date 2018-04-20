from selenium import webdriver

driver = webdriver.Chrome("../selenium/chromedriver")
driver.get("https://sports.yahoo.co.jp/news/list?id=ws")
driver.close()