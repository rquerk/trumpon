# exploring selenium
# idea from da news
# ment for merge fans^^

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
#from selenium.webdriver.support.ui import Select
import sys
import time

# path to browser and adblocker 
browserPath = str(Path.home()) + '/Downloads/geckodriver' 
uBlockPath = str(Path.home()) + '/.mozilla/firefox/naml3cvo.default-release/extensions/uBlock0@raymondhill.net.xpi'
    
# start Adress
address = ''

# pass the pathes to the webdriver
profile = webdriver.FirefoxProfile()
profile.add_extension(extension = uBlockPath)
browser = webdriver.Firefox(executable_path = browserPath, firefox_profile = profile)

class FillCart:
    
    #returning a list of "articles"
    def getArticles(self):
        productList = None
        try:
            productList = browser.find_elements_by_tag_name('article')
        except Exception as e:
            print("no article tag found: ", e.__class__)
            
        return productList
    
    def getItemListByTag(self, tag):
        item = None
        try:
            item = browser.find_elements_by_tag_name(tag)
        except Exception as e:
            print("no {tag} tag found: ", e.__class__)
            
        return item
    
    def addToCart(self):
        AddToCart = browser.find_element_by_name('add');
        # print(AddToCart.text)
        AddToCart.click()
        

if __name__ == "__main__":
    
    cartFiller = FillCart()
    # load main page
    browser.get(address)
    #using sleeps to implement waiting for page loading... not good i know
    time.sleep(2)
    
    productList = cartFiller.getArticles()
    listlen = len(productList)
    
    i = 0
    while True:
        
        if i >= listlen:
            i = 0
        productList = cartFiller.getArticles()
        article = productList[i]
        # print(article.text)
        article.click()
        time.sleep(3)
        cartFiller.addToCart()
        time.sleep(3)
        browser.get(address)
        time.sleep(3)
        
        i = i + 1
    
    browser.quit()
