import requests
from bs4 import BeautifulSoup
import smtplib
URL="https://www.amazon.in/Amazfit-Multisport-Navigation-Waterproof-Monitoring/dp/B0B37T17VM/ref=lp_29375229031_1_8"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response=requests.get(URL,headers=headers)
data=response.text
soup=BeautifulSoup(data,"html.parser")
price=soup.find(name="span",class_="a-price-whole").getText()
title=soup.find(name="span",id="productTitle").getText()
list_of_digits=[digit for digit in price]
list_of_digits.remove(",")
list_of_digits.remove(".")
original_price=int(''.join(list_of_digits))
if original_price>15000:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="xabc31480@gmail.com",password="gxcyhqqqphnlxqny")
    connection.sendmail(from_addr="xabc31480@gmail.com",to_addrs="xabc31480@gmail.com",msg=f"{title} is now {original_price} \n {URL}")
    connection.close()








