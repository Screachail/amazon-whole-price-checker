from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
global browser

s=Service("C:/Users/kacper.szafraniec/Downloads/chromedriver_win32.exe")
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options, service=s)
url="https://www.amazon.com/Instant-Pot-Ultimate-Pressure-Dehydrate/dp/B0B1G5M31V/ref=sr_1_1_sspa?crid=16DNZYFQ3JYQG&" \
    "keywords=instant+pot&qid=1677849412&sprefix=instant+po%2Caps%2C201&sr=8-1-spons&psc=1&spLa=" \
    "ZW5jcnlwdGVkUXVhbGlmaWVyPUFGSEdMQVY3UE8yN1AmZW5jcnlwdGVkSWQ9QTA3MjIzMzQ4S0dCTTIzSkRIWDkmZW5jcnlwdGVkQWRJZD1BMDY" \
    "yNTc4NTM4TU5IM0U0TzFLUkwmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
browser.get(url)

price_parent = browser.find_element(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")
price = price_parent.text


print(f"The price is: {price}$")
browser.quit()


