# from lxml import html
import random, requests, time#, subprocess


print("Hello, World!")

def ApiIP ():
    while True:
        try:
            response = requests.post('https://api.myip.com', json={'key':'value'}, timeout=3)
            print(response.json()['ip'])
            break
        except:
            time.sleep(1)
            print("Error")

ApiIP ()
