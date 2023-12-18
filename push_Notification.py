import requests
import os
_TOKEN = "6538080926:AAFMORmrgG5Bh0Ri7ng4MX8HJ47lhxVGajE"


# def send_photo():
#     data = {"chat_id": '6538080926', "caption": '''
# Badbot.AI🇰🇭 has been updated with Google Gemin. 
# New Feature:
# - Chat Assistance (Q & A)
# - Text Generate
# - Code Recognize and Generate
# - Image Recognition
# - Image Q & A'''}
#     url = f"https://api.telegram.org/bot{_TOKEN}/sendPhoto?chat_id={'6538080926'}"
#     with open('gemini.png', "rb") as image_file:
#         ret = requests.post(url, data=data, files={"photo": image_file})
#     print(ret.json())


def send_photo():
    data = {"chat_id": '673968568', "caption": '''
 Badbot.AI🇰🇭 has been updated with Google Gemini. 
 New Feature:
 - Chat Assistance (Q & A)
 - Text Generate
 - Code Recognize and Generate
 - Image Recognition
 - Image Q & A'''}
    url = f"https://api.telegram.org/bot{_TOKEN}/sendPhoto?chat_id={'673968568'}"
    with open('gemini.png', "rb") as image_file:
        ret = requests.post(url, data=data, files={"photo": image_file})
    print(ret.json())


send_photo()
