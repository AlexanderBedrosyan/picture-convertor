from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


edge_driver_path = 'D:/edge_driver/msedgedriver.exe'
service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)


try:
    driver.get("https://heic.online/")
    wait = WebDriverWait(driver, 10)
    consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')))
    consent_button.click()
    upload_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="zbasic"]/button')))
    time.sleep(60)
except:
    print('Not working! Please check the XPATH or edge driver path! Be aware that you have install the webdriver before starting the script!')


def find_all_heic_pictures(needed_path):
    """Find all heic pictures in the path. The path is set to the main folder directory, it can be changed manually"""
    heic_pictures = []
    for file in os.listdir(needed_path):
        if file.lower().endswith('.heic'):
            heic_pictures.append(f'{needed_path}\{file}')
            heic_file = f'{needed_path}\{file}'
            jpeg_file = f'image.JPEG'

            command = f"magick convert {heic_file} {jpeg_file}"

    return heic_pictures


path = os.getcwd()
all_heic_pictures = find_all_heic_pictures(path)
print(all_heic_pictures[0])
