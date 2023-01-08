from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# driver.get("https://chaldal.com/meat-new")

totalPage = 25
totalProduct = 40

titleList = []
priceList = []
reviewList = []
ratingList = []
commentList = []

for i in range(1, totalPage+1):
    driver.get("https://www.daraz.com.bd/mens-t-shirts/?page="+str(i)+"&spm=a2a0e.searchlistcategory.cate_4_1.1.3f907d09BBE7ui")
    for j in range(1,totalProduct+1):
        productLink = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div['+str(j)+']/div/div/div[2]/div[2]/a')
        proLink = productLink.get_attribute('href')
        driver.switch_to.new_window()
        driver.get(proLink)
        title = driver.find_element(by=By.XPATH, value='//*[@id="module_product_title_1"]/div/div/span')
        price = driver.find_element(by=By.XPATH, value='//*[@id="module_product_price_1"]/div/div/span')
        try:
            review = driver.find_element(by=By.XPATH, value='//*[@id="module_product_review_star_1"]/div/a[1]')
        except NoSuchElementException:
            review = driver.find_element(By.XPATH, value='//*[@id="module_quantity-input"]/div/div/h6')
        try:
            comment = driver.find_element(by=By.XPATH, value='//*[@id="module_product_review_star_1"]/div/a[2]')
        except NoSuchElementException:
            comment = driver.find_element(By.XPATH, value='//*[@id="module_quantity-input"]/div/div/h6')
        driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(1)
        try:
            rating = driver.find_element(By.XPATH, value='//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]')
        except NoSuchElementException:
            rating = driver.find_element(By.XPATH, value='//*[@id="module_quantity-input"]/div/div/h6')

        titleList.append(title.text,)
        priceList.append(price.text,)
        reviewList.append(review.text,)
        ratingList.append(rating.text, )
        commentList.append(comment.text, )

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

# print(titleList)

data = {'Product Name': titleList,
        'Price': priceList,
        'Rating (5)': ratingList,
        'Comment/Questions': commentList,
        'Reviews Count': reviewList,
        }


df = pd.DataFrame(data)

df.to_csv(r'G:\EuropeanITSoulution\Class 24\darazDataScrape\scrapeData4.csv', index=False)


driver.quit()
