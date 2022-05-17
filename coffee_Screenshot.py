#selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
from PIL import Image
from screenshot import Screenshot_Clipping
ss = Screenshot_Clipping.Screenshot()

import time
import os
import json

#driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
#driver.get('https://filfox.info/en/') # website link
#driver.execute_script("document.body.style.zoom='50%'") #website zoom 
#time.sleep(5) # Let the user actually see something!

#dictionary of the name and address it belongs to 
x = {
   "wang": ["f01111881","f01464670","f01154375","f01034007","f01501599","f01589943"],
   "shen": ["f01054527","f01177326"],
   "mark":["f01265322","f01137193"],
   "chen":["f01464400","f01372569","f01597362","f01445415","f01698865","f01771575"],
   "ben":["f01264903"],
   "deng":["f01316365"],
   "coffeecloud":["f01807413","f01822659","f01845913"],
   "mei":["f01624906","f01782079","f01831595"],
   "ivan":["f01727648","f01768764"],
   "shenzhen":[""]

}

y = json.dumps(x)
data = json.loads(y)
address_dic = data

def screenshot_filfox(address):
    #address_input = input("Enter your address")
    #tala ko line ma chai pass garnu parne 
    print(address.keys())
    for name in address.keys():
        #os.mkdir(f'/Users/sayonrai/CC/dailydata/{name}')
        for addr in address[name]:
            url = "https://filfox.info/en/"
            driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
            driver.get(url) # website link
            driver.implicitly_wait(3)
            driver.execute_script("document.body.style.zoom='50%'") #website zoom 
            print(f'{name} {addr}')
            time.sleep(5)
            search_box = driver.find_element_by_xpath('//*[@id="__layout"]/div/nav/div[2]/div[5]/input')
            search_box.send_keys(addr)
            #for loop chalako pass vaye ni number matra hunxa 'f01111881' pass hudaina
            search_box.send_keys(Keys.RETURN)
            time.sleep(5) # Let the user actually see something!
            #takes screenshot
            image = ss.full_Screenshot(driver, save_path= f'/Users/sayonrai/CC/dailydata/{name}', image_name=f'{addr}.png')
            #screen = Image.open(image)
            #screen.show()
            
            #refresh
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
            time.sleep(3)
            """
            owner_address = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[6]/div/div[2]/div[2]/a')
            owner_address.click()
            """


screenshot_filfox(address_dic)


