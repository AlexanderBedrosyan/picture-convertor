from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from heic_finder import *
from typing import List


def used_web_for_changing_the_format(all_heic_pictures=List):
    edge_driver_path = 'D:/edge_driver/msedgedriver.exe'
    service = EdgeService(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)


    try:
        driver.get("https://heic.online/")
        wait = WebDriverWait(driver, 10)

        consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')))
        consent_button.click()

        time.sleep(2)

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/main/article/div/div[1]/div/div/div/form/input[2]')))

        for pic_path in heic_picture_list:

            file_input.send_keys(pic_path)

        time.sleep(5)

        check_box_consent = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/main/article/div/div[4]/input')))
        check_box_consent.click()

        time.sleep(2)
        convert_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/main/article/div/p[1]/button')))
        convert_button.click()

        time.sleep(2)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/main/article/div/div[2]/div/button[1]')))
        download_button.click()

        time.sleep(15)
    except:
        print('Not working! Please check the XPATH or edge driver path! Be aware that you have install the webdriver before starting the script!')


heic_picture_list = find_all_heic_pictures()
used_web_for_changing_the_format(heic_picture_list)
