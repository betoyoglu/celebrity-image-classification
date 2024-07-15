import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp")
search_box= driver.find_element(By.CSS_SELECTOR, '.gLFyf[name="q"]').send_keys("lee taeyong", Keys.ENTER)

time.sleep(5)

# Resimlerin dinamik olarak yüklenmesini sağlamak için sayfayı aşağı kaydır
for _ in range(2): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) 

# Resim elementlerini bulun
image_elements = driver.find_elements(By.CSS_SELECTOR, '.YQ4gaf img[src]')

# İlk 5 resim URL'sini al ve indir
for index, img in enumerate(image_elements[:5]):
    try:
        img_url = img.get_attribute('src')
        if img_url:
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                with open(f"taeyong{index}.jpg", 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
            else:
                print(f"Error downloading image {img_url}: status code {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

driver.quit()