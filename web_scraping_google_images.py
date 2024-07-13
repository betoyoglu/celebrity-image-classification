from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Selenium WebDriver'ı başlat
driver = webdriver.Chrome()

# Google Resimler sayfasını aç
driver.get('https://www.google.com/imghp')

# Arama kutusunun yüklenmesini bekle
time.sleep(3)  # Gerekirse süreyi ayarlayabilirsiniz

# Arama kutusunu bul ve "cats" yazarak arama yap
search_box = driver.find_element(by='css selector', value='input[name="q"]')
search_box.send_keys('cats')
search_box.submit()

# Sayfanın tamamının yüklenmesini bekleyin (gerektiğinde süreyi ayarlayabilirsiniz)
time.sleep(5)

# Sayfa kaynağını alın
page_html = driver.page_source

# BeautifulSoup ile sayfa kaynağını işleyin
soup = BeautifulSoup(page_html, 'html.parser')

# Tüm resim konteynerlerini bulun
image_containers = soup.find_all('img')

# Her bir resim için işlem yapın
for index, img in enumerate(image_containers):
    try:
        # Resmin URL'sini alın
        img_url = img['src']
        
        # Resmi indirin
        response = requests.get(img_url)
        img_data = response.content
        
        # Resmi Pillow kütüphanesi ile açın ve ekrana yazdırın
        img = Image.open(BytesIO(img_data))
        img.show()
        
        # Her bir resim için bir dosyaya kaydetmek için bu kısmı kullanabilirsiniz
        # file_name = f"image_{index}.jpg"
        # with open(file_name, 'wb') as f:
        #     f.write(img_data)
        
    except Exception as e:
        print(f"Hata alındı: {str(e)}")

# WebDriver'ı kapat
driver.quit()
