##################### Extra Hard Starting Project ######################
import pandas
import datetime
import os
import random
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data=pandas.read_csv("birthdays.csv",index_col=False)
dict=data.to_dict()



month=dict["month"][0]
day=dict["day"][0]
name=dict["name"][0]
email=dict["email"][0]



now=datetime.datetime.now()
if now.month==month and now.day==day:
    with open(f"C:/Users/Admin/PycharmProjects/birthday/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt") as file:
        data=file.readlines()
        data[0] = f"Dear {name}"
    wishes=""
    for item in data:
        wishes+=item

    my_email = "xabc31480@gmail.com"
    password = "bzbgtmnackvfwgkh"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=f"{email}", msg=f"Subject:Birthday wishes\n\n{wishes}")
    connection.close()









# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




