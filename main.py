from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.purina.ru/find-a-pet/cat-breeds"
driver.get(url)

breeds = driver.find_elements(By.CLASS_NAME, 'breed-card')
cat_breeds = []

for breed in breeds[:24]:
    name = breed.find_element(By.TAG_NAME, 'h3').text.strip()
    description = breed.find_element(By.TAG_NAME, 'p').text.strip()
    cat_breeds.append({'name': name, 'description': description})

for breed in cat_breeds:
    print(f"Порода: {breed['name']}")
    print(f"Описание: {breed['description']}\n")

driver.quit()