# had tuntime error on jupyter kernal

#!/bin/python3
import requests
from bs4 import BeautifulSoup as BS
url1="https://www.amazon.in/s?k=top+10+phones+under+20000&crid=3UFKG06L1X1O1&sprefix=top+10+phone%2Caps%2C310&ref=nb_sb_ss_i_4_12"
url2="https://www.amazon.in/Test-Exclusive-712/dp/B07DJCJBB3/ref=sr_1_1_sspa?crid=3UFKG06L1X1O1&dchild=1&keywords=top+10+phones+under+20000&qid=1600098521&sprefix=top+10+phone%2Caps%2C310&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFZRWlZXUDZKNFNOJmVuY3J5cHRlZElkPUEwODUxMTQ3MlJRTkhESldaUFE1VyZlbmNyeXB0ZWRBZElkPUEwNzg3ODkwMVg2RFdCSFFPNjY4TCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU"

from requests_html import HTMLSession
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
session = HTMLSession()
r = session.get(url1,headers=headers,timeout=3)
if r.ok:
    print("Got the page ...\n rendering" )
    r.html.render(scrolldown=10,sleep=1) # do a scrool down and a 3 sec sleep
    print("completed js rendering")
# print(r.html.search("a-price-whole"))
#########################

print()
print()

# print(r.html.search("div.a-price-whole"))
# print(type(r.html.search("div.a-price-whole")))


match=r.html.find('#search > div.s-desktop-width-max.s-opposite-dir > div > div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28')
print(match)
print(len(match))
print()
print()
matched_phones= r.html.find("#search > div.s-desktop-width-max.s-opposite-dir > div > div.sg-col-20-of-24.s-matching-dir.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(1)")
print(len(matched_phones))

for eachphone in matched_phones:
    price=eachphone.find(".a-price-whole")
    # >>> x=match.find(".a-price-whole")
    print(price)



