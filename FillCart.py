"""
exploring selenium. The script is ment for merge fans^^
products probably won't be reserved before you attempt to
actually buy stuff.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
#from selenium.webdriver.support.ui import Select
import sys
import time

# path to browser and adblocker 
browserPath = str(Path.home()) + '/Downloads/geckodriver' 
uBlockPath = str(Path.home()) + '/.mozilla/firefox/naml3cvo.default-release/extensions/uBlock0@raymondhill.net.xpi'
    
address = 'https://shop.donaldjtrump.com'

# for the extension we need such profile
profile = webdriver.FirefoxProfile()
profile.add_extension(extension = uBlockPath)
browser = webdriver.Firefox(executable_path = browserPath, firefox_profile = profile)

def getArticles():
    productList = None
    try:
        productList = browser.find_elements_by_tag_name('article')
    except Exception as e:
        print("no article tag found: ", e.__class__)
            
    return productList
    
def getItemListByTag(tag):
    item = None
    try:
        item = browser.find_elements_by_tag_name(tag)
    except Exception as e:
        print("no {tag} tag found: ", e.__class__)
        
    return item
    
def addToCart():
    AddToCart = browser.find_element_by_name('add')
    AddToCart.click()
        

if __name__ == "__main__":
    
    browser.get(address)
    
    productList = getArticles()
    listlen = len(productList)
    
    # iterator over product list
    i = 0
    while :
        
        if i >= listlen: 
            i = 0
            
        productList = getArticles()
        article = productList[i]
        article.click()
        addToCart()
        browser.get(address)
        
        i = i + 1
    
    browser.quit()
