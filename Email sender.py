import random
import smtplib

# my_email="xabc31480@gmail.com"
# password="bzbgtmnackvfwgkh"
# 
# connection=smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="pushpaks59@yahoo.com",msg="Subject:hello\n\nThis is the body of my email")
# connection.close()

with open ("quotes.txt",mode="r") as file:
    data=file.readlines()
quotes_list=[quote for quote in data]

import datetime

time=datetime.datetime.now()
if time.weekday()==2:
    quote=random.choice(quotes_list)


    my_email="xabc31480@gmail.com"
    password="bzbgtmnackvfwgkh"

    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="pushpaks59@yahoo.com",msg=f"Subject:motivation\n\n{quote}")
    connection.close()

