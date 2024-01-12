import logging
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys
from datetime import datetime, timedelta
import calendar
import json
import os
import csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def selenium_function(apart_id):
    # print(driver, 'see driver status')
    try: 
        driver = webdriver.Chrome()
        # Open the URL
        driver.get(apart_id)
        
        # driver.get("https://nigeriapropertycentre.com/for-rent/flats-apartments/lagos/lekki/osapa/2065781-serviced-2-bedroom-apartment")

        # Find an element by its ID
        element_by_id = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[1]/h4")
        
        location = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[1]/address")
        
        # concatenate three together
        tag = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/span/span[1]")
        price = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/span/span[2]")
        annum = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/span/span[3]")
        
        bedroom = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[2]/span[1]")
        mors = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[1]/span[2]")
        
        bathroom = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[2]/span[1]")
        baths = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[2]/span[2]")

        # Now you can work with the located element
        print("Text content of the element:", element_by_id.text)
        print("location", location.text)
        print(tag.text + price.text, "PRICE")
        bedplmors = bedroom.text + " " + mors.text
        mathplmore = bathroom.text + " " + baths.text
        print("annum", annum.text)
        
        data = [["description", "location", "price", "bedroom", "bathroom", "yearly"], [element_by_id.text, location.text, price.text, bedplmors, mathplmore, annum.text]]
        print(data)
        
        csv_filename = 'example.csv'
        
        with open(csv_filename, mode="a", newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow(data[0])
            
            writer.writerow(data[1])
            
    finally:
        # Close the browser window
        driver.quit()
        
if __name__ == '__main__':
    pass