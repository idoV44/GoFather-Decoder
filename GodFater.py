import bs4, requests
from Crypto.Cipher import Blowfish
import base64
import random
import string
import sys
import requests
import pyperclip
import sys



print('''                      888 .d888        888   888                     
                     888d88P"         888   888                     
                     888888           888   888                     
 .d88b.  .d88b.  .d88888888888 8888b. 88888888888b.  .d88b. 888d888 
d88P"88bd88""88bd88" 888888       "88b888   888 "88bd8P  Y8b888P"   
888  888888  888888  888888   .d888888888   888  88888888888888     
Y88b 888Y88..88PY88b 888888   888  888Y88b. 888  888Y8b.    888     
 "Y88888 "Y88P"  "Y88888888   "Y888888 "Y888888  888 "Y8888 888     
     888                                                            
Y8b d88P                                                            
 "Y88P" \n''')

itemurl = pyperclip.paste()
status=""
registered_check = open("xxx/GodFather_reg.txt", "r")

response = requests.get(itemurl,headers={'User-Agent': 'Mozilla/5.0'})

soup = bs4.BeautifulSoup(response.text,features="html.parser")
soupnew=str(soup)
resultCodeBegin=soupnew.split('<div class="tgme_page_description" dir="auto">')
resultCodeEnd=resultCodeBegin[1].split("</div>")
resultCode=resultCodeEnd[0]

msg = Blowfish.new(b'ABC').decrypt(base64.b64decode(resultCode))
msgToStr=str(msg)
resultURLParts=msgToStr.split('/')
resultURL="http://"+resultURLParts[2]
print(resultURL)

url="xxx"
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
endPath=["/g0df4th3r.php","/porookza.php", "/kataram.php", "/patara.php", "/cavarak.php"]
for i in range (0,len(endPath)):
    parturl = resultURL+endPath[i]
    response = requests.get(parturl,headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        url = resultURL+endPath[i]
        path=endPath[i]
    

if url=="xxx":
    print("There is no path exist")    
    sys.exit()

if url in registered_check.read():
    status="This attack is already registered!!!!"
    registered_check.close() 

else:    
    registered = open("xxx/GodFather_reg.txt", "a")
    registered.write(url)
    registered.close()

response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})


data = {
    "Host": resultURLParts[2],
    "country": "us",
    "new": "true",
    "ver": "8.1.0",
    "applist": "com.xxx|||",
    "key": key
}

response = requests.post(url, data)
new_response = response.text.replace(",", "\n" )






print("the Trigers are:")
print(new_response)
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")
print(response)
print("The host is: "+ data["Host"])
print("The country of the machime is: "+ data["country"])
print("The version is: "+ data["ver"])
print("The folder and file path is: "+ path)
print("The full URL is: "+ url)
if(status!=""):
    print("ALERT: "+status)





