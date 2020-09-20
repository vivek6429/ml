# had tuntime error on jupyter kernal

#!/bin/python3

# from bs4 import BeautifulSoup as BS
print("\nincase of NameError: name 'pyppeteer' is not defined --- RE RUN PROGRAM \n\n\n\n ")

from requests_html import HTMLSession
import pandas as pd
import numpy as np
import os

url1="https://www.amazon.in/s?k=top+10+phones+under+20000&crid=3UFKG06L1X1O1&sprefix=top+10+phone%2Caps%2C310&ref=nb_sb_ss_i_4_12"
url2="https://www.amazon.in/Test-Exclusive-712/dp/B07DJCJBB3/ref=sr_1_1_sspa?crid=3UFKG06L1X1O1&dchild=1&keywords=top+10+phones+under+20000&qid=1600098521&sprefix=top+10+phone%2Caps%2C310&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFZRWlZXUDZKNFNOJmVuY3J5cHRlZElkPUEwODUxMTQ3MlJRTkhESldaUFE1VyZlbmNyeXB0ZWRBZElkPUEwNzg3ODkwMVg2RFdCSFFPNjY4TCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
session = HTMLSession()
try :
    r = session.get(url1,headers=headers,timeout=3)
except:
    print("error occured during GET operation")

print("Page response :",r.status_code)
    
if r.ok:
    print("Got the page ...\nrendering\n may take time \nfirst run will download chromium " )
    try:
        r.html.render() # do a scrool down and a 3 sec sleep
    except pyppeteer.errors.TimeoutError:
        print("TimeoutError..... exiting")
        exit()

    print("completed js rendering")



##########################################THIS SELECTS ENTIRE PHONES
matched_phones = r.html.find(".sg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28") 
print("Found ",len(matched_phones),"phone details")

##########################################CREATING DATAFRAME
column_names = ["name", "price", "discount","delivery_details","deliveryby_day","emi_details","prime_delivery","image"]
df = pd.DataFrame(columns = column_names)



def extract_imagelink(x):
    try:
        src=str(x[0].attrs["src"])
    except:
        src="Was_unable_to_extract"
    return src          

def prime_checker(p):
    if p==[]:
        return False # we got empty data
    else:
        return True # this data is present on the webpage

    return "Something_went_wrong"
    pass


def add_2df(info_list,prime,image):#name,price,discount,delidet,deliveryby_day,emi,-----------prime,image
    df_length = len(df)
    df_appendlist=[]
    for eachinfo in info_list:
        if eachinfo == []:
            df_appendlist.append("NA")
        else :
            try :
                
                df_appendlist.append(str(eachinfo[0].text))

                
            except :
                print("some error occured during :str(eachinfo[0].text) ")
                df_appendlist.append("NA")

            
    df_appendlist.append(prime_checker(prime))
    df_appendlist.append(extract_imagelink(image))
    # finaly appending data
    df.loc[df_length] = df_appendlist
    #print(*df_appendlist,sep="\n")
    
    
        
    

#THE RETURN OBJECTS ARE AS LIST
for eachphone in matched_phones:
    infolist=[]
    name=eachphone.find(".a-size-medium")
    infolist.append(name)
    
    price=eachphone.find(".a-price-whole")
    infolist.append(price)

    discount=eachphone.find(".a-letter-space+ span")
    infolist.append(discount)

    deliverydetails=eachphone.find(".s-align-children-center+ .a-row")
    infolist.append(deliverydetails)

    deliveryby_day=eachphone.find(".s-align-children-center .a-text-bold")
    infolist.append(deliveryby_day)

    emidetails=eachphone.find(".a-truncate-cut")
    infolist.append(emidetails)

    prime=eachphone.find(".s-prime .a-icon-medium")
    image=eachphone.find(".s-image-fixed-height .s-image")

    #print(infolist[0])
    #print(str(infolist[0]))
    add_2df(infolist,prime,image)

    
    try:
        print(name[0].text,"  ",price[0].text,"\n ",discount[0].text," ",deliverydetails[0].text,"\n ",emidetails[0].text)
    except :
        print("ee-- some missing vals")
              

print(df)
try:
    # add this file to .gitignore
    print("Writing file")
    print("check install xlsxwriter in case of error")
    # writing to excel
    writer = pd.ExcelWriter('phones_out.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    
except:
    print("Write error")
session.close()
input("Press Enter to continue...")
    
