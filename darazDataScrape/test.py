from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.daraz.com.bd/womens-dresses/?page=1&page12&spm=a2a0e.searchlistcategory.cate_1_1.1.543b2e5crb6BTm")

ratingList = []
for i in range(1,3):
    #driver.get("https://www.daraz.com.bd/womens-dresses/?page=1&page12&spm=a2a0e.searchlistcategory.cate_1_1.1.543b2e5crb6BTm")
    # driver.execute_script("window.scrollTo(0, 1100)") 
    # time.sleep(1)
    productLink = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(i)+']/div/div/div[2]/div[2]/a')
    egtL = productLink.get_attribute('href')
    #print(productLink.text) 
    driver.switch_to.new_window()
    driver.get(egtL)
    driver.execute_script("window.scrollTo(0, 1200)") 
    #rating = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]')
    time.sleep(1)
    #no such element: Unable to locate element
    try: 
        rating = driver.find_element(By.XPATH, '//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]')
    except NoSuchElementException:
        rating = driver.find_element(By.XPATH, '//*[@id="module_quantity-input"]/div/div/h6')

    print(rating.text) 
    ratingList.append(rating.text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(1) 


data = {
        'Rating (5)': ratingList,
        }


df = pd.DataFrame(data)

df.to_csv(r'G:\EuropeanITSoulution\Class 24\darazDataScrape\scrapeData.csv', index=False)
