import time

import requests
from datetime import datetime
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
MY_LAT = 38.846226 # Your latitude
MY_LONG = -77.306374 # Your longitude
#

# connection.starttls()
# connection.login(user=my_email, password=password)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_pos = (iss_latitude, iss_longitude)
print(iss_pos)
    #Your position is within +5 or -5 degrees of the ISS position.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/maps')
time.sleep(5)
search = driver.find_element(By.ID, "searchboxinput")
search.send_keys(f"{iss_latitude}, {iss_longitude}")
search.send_keys(Keys.ENTER)


# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
#     time_now = datetime.now().hour
#     if time_now >=sunset or time_now <= sunrise:
#         return True
#
# while True:
#     time.sleep(60)
#     if is_iss_overhead and is_night:
#         connection.sendmail(from_addr=my_email, to_addrs="pal_patel21@yahoo.com", msg="Subject: Look Up \n\n Look up")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



