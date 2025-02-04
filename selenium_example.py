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
for _ in range(5): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2) 

# Resim elementlerini bulun
image_elements = driver.find_elements(By.CLASS_NAME, 'YQ4gaf')

save_dir = "baekhyun_images"
os.makedirs(save_dir, exist_ok=True)

time.sleep(2)

count = 0
min_width, min_height = 100, 100  # Minimum resim boyutları

for img in image_elements:
    if count >= 250:
        break

    img_url = img.get_attribute("src")

    if img_url and img_url.startswith("data:image/jpeg;base64,"):
        img_data = img_url.replace("data:image/jpeg;base64,", "")
        img_data = base64.b64decode(img_data)
        
        # Image boyut kontrolü
        image = Image.open(BytesIO(img_data))
        if image.width < min_width or image.height < min_height:
            continue
        
        img_path = os.path.join(save_dir, f"baekhyun_{count}.jpg")
        with open(img_path, "wb") as f:
            f.write(img_data)
        print(f"Resim {count} kaydedildi: {img_path}")
        count += 1

    elif img_url and (img_url.startswith("http://") or img_url.startswith("https://")):
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                img_data = response.content
                
                # Image boyut kontrolü
                image = Image.open(BytesIO(img_data))
                if image.width < min_width or image.height < min_height:
                    continue
                
                img_path = os.path.join(save_dir, f"baekhyun_{count}.jpg")
                with open(img_path, "wb") as f:
                    f.write(img_data)
                print(f"Resim {count} kaydedildi: {img_path}")
                count += 1
            else:
                print(f"Geçersiz URL (status code {response.status_code}): {img_url}")
        except Exception as e:
            print(f"Resim indirilemedi: {img_url} hata: {str(e)}")
    else:
        print(f"Geçersiz URL: {img_url}")
driver.quit()