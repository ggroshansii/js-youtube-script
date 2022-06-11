from flask import Flask, jsonify, request
from flask_cors import CORS

import requests
from bs4 import BeautifulSoup

import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By

import time

app = Flask(__name__)
CORS(app)


transcript = []

@app.route("/")
def parse_html():

    print('fired', len(transcript))
    driver = webdriver.Chrome()
    hello = driver.get("https://www.youtube.com/watch?v=o5Mwa_TJ3HM")
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(10) # gives an implicit wait for 20 seconds
    print("URL", hello)
    driver.find_element(By.XPATH, '//ytd-menu-renderer/yt-icon-button/button/yt-icon').click()
    driver.implicitly_wait(5)
    dropdown = driver.find_element(By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer').click()
    text = driver.find_elements(By.CLASS_NAME, "segment-text")
    
    for i in text:
        print(i.text)
        transcript.append(i.text)
    
    time.sleep(3)
    driver.close()
        
    print(transcript)

    return jsonify(response="Hello World")
