#selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
from PIL import Image
from Screenshot import Screenshot_Clipping
ss = Screenshot_Clipping.Screenshot()

import time
import os
import json

#driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
#driver.get('https://filfox.info/en/') # website link
#driver.execute_script("document.body.style.zoom='50%'") #website zoom 
#time.sleep(5) # Let the user actually see something!

#dictionary of the name and address it belongs to 

address_dic = {
    #"wang":"f01111881",
    #"wang1":"f01464670",
    #"wang2":"f01154375",
    #"wang3":"f01034007",
    #"wang4":"f01501599","wang5":"f01589943",
    #"shen":"f01054527","shen1":"f01177326",
    #"mark":["f01265322"],
    #"chen":['f01464400','f01372569','f01597362','f01445415','f01698865','f01771575'],
    #"ben":['f01264903'],
    "deng":["f01316365"],
    "coffeecloud":["f01807413"],
    "su":["f01624906","f01782079"],
    "rollingstone":["f01626808","f01716971"],
    "Mr.li":["f01700446"],
    "ivan":["f01727648","f01768764"]
   
    }

def wang_screenshot_filfox(address):
    #address_input = input("Enter your address")
    print(address.keys())
    for name in address.keys():
        #os.mkdir(f'/Users/sayonrai/CC/dailydata/{name}')
        for address in address[name]:
            url = "https://filfox.info/en/"
            driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
            driver.get(url) # website link
            driver.implicitly_wait(3)
            driver.execute_script("document.body.style.zoom='50%'") #website zoom 
            print(f'{name} {address}')
            time.sleep(5)
            search_box = driver.find_element_by_xpath('//*[@id="__layout"]/div/nav/div[2]/div[5]/input')
            search_box.send_keys(address)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5) # Let the user actually see something!
            #takes screenshot
            image = ss.full_Screenshot(driver, save_path= f'/Users/sayonrai/CC/dailydata/{name}', image_name=f'{address}.png')
            #screen = Image.open(image)
            #screen.show()
            
            #refresh
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
            time.sleep(3)
            #click address link
            owner_address = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[6]/div/div[2]/div[2]/a')
            owner_address.click()


wang_screenshot_filfox(address_dic)


