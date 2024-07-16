import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin
import os 
import base64

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp")
search_box= driver.find_element(By.CSS_SELECTOR, '.gLFyf[name="q"]').send_keys("byun baekhyun", Keys.ENTER)

time.sleep(5)

# Resimlerin dinamik olarak yüklenmesini sağlamak için sayfayı aşağı kaydır
for _ in range(2): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) 

# Resim elementlerini bulun
image_elements = driver.find_elements(By.CLASS_NAME, 'YQ4gaf')

save_dir = "baekhyun_images"
os.makedirs(save_dir, exist_ok=True)

time.sleep(2)

for i, img in enumerate(image_elements[:300]):
    img_url = img.get_attribute("src")
    
    if img_url.startswith("data:image/jpeg;base64,"):
        img_data = img_url.replace("data:image/jpeg;base64,", "")
        img_data = base64.b64decode(img_data)
        
        img_path = os.path.join(save_dir, f"baekhyun_{i}.jpg")
        with open(img_path, "wb") as f:
            f.write(img_data)
        print(f"Resim {i} kaydedildi: {img_path}")
    else:
        print(f"Resim {i} için geçersiz URL: {img_url}")

driver.quit()