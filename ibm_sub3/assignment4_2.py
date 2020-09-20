# had tuntime error on jupyter kernal

#!/bin/python3

# from bs4 import BeautifulSoup as BS

from requests_html import HTMLSession
import pandas as pd
import numpy as np
import os

url1="https://www.amazon.in/s?k=top+10+phones+under+20000&crid=3UFKG06L1X1O1&sprefix=top+10+phone%2Caps%2C310&ref=nb_sb_ss_i_4_12"
url2="https://www.amazon.in/Test-Exclusive-712/dp/B07DJCJBB3/ref=sr_1_1_sspa?crid=3UFKG06L1X1O1&dchild=1&keywords=top+10+phones+under+20000&qid=1600098521&sprefix=top+10+phone%2Caps%2C310&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFZRWlZXUDZKNFNOJmVuY3J5cHRlZElkPUEwODUxMTQ3MlJRTkhESldaUFE1VyZlbmNyeXB0ZWRBZElkPUEwNzg3ODkwMVg2RFdCSFFPNjY4TCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
session = HTMLSession()
try :
    r = session.get(url2,headers=headers,timeout=3)
except:
    print("error occured during GET operation")

print("Page response :",r.status_code)
    
if r.ok:
    print("Got the page ...\n rendering\n may take time \n first run will download chromium " )
    try:
        r.html.render() # do a scrool down and a 3 sec sleep
    except pyppeteer.errors.TimeoutError:
        print("TimeoutError..... exiting")
        exit()

    print("completed js rendering")






#######################################LOOKINF FOR PAGE WITH ALL REVIEWS
print("Moving to page with all reviews")
session2 = HTMLSession()



match=r.html.find(".a-link-emphasis.a-text-bold")
if len(match) !=1:
    print ("ambiguity....iam...exiting")
    exit()
    
# jumping onto to the entire review page
url2_="https://www.amazon.in"+match[0].attrs["href"]

try :
    r = session2.get(url2_,headers=headers,timeout=3)
except:
    print("error occured during GET operation")

print("Second Page response :",r.status_code)
    
if r.ok:
    print("\n\n\nGot the second page ...\n rendering " )
    try:
        r.html.render() # do a scrool down and a 3 sec sleep
    except pyppeteer.errors.TimeoutError:
        print("TimeoutError..... exiting")
        exit()

    print("completed js rendering \n\n\n\n")




    
##########################################THIS selector css
# The top posetive and negative are inside   #cm_cr-rvw_summary-viewpoints .view-point
#-----------dont bother they come up as first and second entries anyway

# # author name                 .a-profile-name
# # review rating               .review-rating
# # review title

# try divide and conqour ---------
####THE ENTRIES ARE IN : class :  a-section review aok-relative
# now ,
# # author name                 .a-profile-name
# # author profile icon          .a-profile-avatar
# # author profile link         check attribute inside this
# # review rating star              .review-rating
# # review date                    .review-date
#
# main content                 class="a-size-base review-text review-text-content"
# reviewed images              review-image-tile-section

##########################################CREATING DATAFRAME
column_names = ["authorname", "icon_image", "review_rating_star","review_details","review_main","images_links"]
df = pd.DataFrame(columns = column_names)


#############################################################

reviews=r.html.find(".a-section.review.aok-relative") 
print("found out ",len(reviews)," number of review(s)")
############################################################
for each_review in reviews:
    author_name=each_review.find(".a-profile-name")
    author_name=author_name[0].text
    author_icon=each_review.find(".a-profile-avatar")  
    author_icon=author_icon[0].find("img")[0].attrs["src"]  # everithing is a list of <class 'requests_html.Element'>

    star_rating=each_review.find(".review-rating")
    star_rating=star_rating[0].find(".a-icon-alt") # moving one more level down
    star_rating=star_rating[0].text

    review_date=each_review.find(".review-date")
    review_date=review_date[0].text

    main_content=each_review.find(".a-size-base.review-text.review-text-content")[0].text

    images_links= " "

    images=each_review.find(".review-image-tile")
    for image in images:
        try :
            images_links = images_links+"  "+str(image.attrs["src"])
        except :
            print(" why did i use this")
    

    df=df.append({"authorname":author_name, "icon_image":author_icon, "review_rating_star":star_rating,\
                  "review_details":review_date,"review_main": main_content , "images_links":images_links }, ignore_index=True)
                  
    appendlist=[author_name,author_icon,star_rating,review_date,main_content,images_links]
    print(*appendlist,sep="\n")
   

print(df)

print("do a pip  install xlsxwriter")
# writing to excel
writer = pd.ExcelWriter('reviews_out.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()




