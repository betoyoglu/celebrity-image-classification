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
for _ in range(3):  # 3 kez aşağı kaydırarak daha fazla resim yükleyin
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Sayfanın yüklenmesini bekleyin

# Resim elementlerini bulun
image_elements = driver.find_elements(By.CSS_SELECTOR, '.czzyk XOEbc')

# İlk 5 resim URL'sini al ve indir
for index, img in enumerate(image_elements[:5]):
    try:
        img_url = img.get_attribute('g-img')
        if img_url is None:
            img_url = img.get_attribute('data-src')
        if img_url:
            response = requests.get(img_url)
            with open(f"taeyong{index}.jpg", 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f"Hata oluştu: {e}")

# WebDriver'ı kapat
driver.quit()