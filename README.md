# trumpon
A first Selenium script [Python]


This script will fill a shopping cart from a very specific merge shop
on a very simple way.

It wont stop until an error occures. So the cart should become larger and larger.
It works on shops that have various "articles" on thier main page, 
and if you click one, you get forwarded to a page containing an "Add To Cart" Button.
But be aware, stuff probably wont be reserved for you before you send some
credentials.


To try it out, you need the geckodriver or a similar browser-driver (gecko is for firefox),
and paste its path into FillCart.py in line 15 after "browserPath =".
Default is "~/Downloads/geckodriver" 

I also used my alreaddy installed uBlockOrigin add blocker.
So if you run linux and have this extension added to firefox,
you probably have the same file location like me, but better check that in line 16.

For Windows you need to change both pathes for sure.
If you want to use Chrome or any other driver, you need to change line 20 and 22.





This script needs improvement,
next thing should be a propper waiting for the web pages to be fully loaded
