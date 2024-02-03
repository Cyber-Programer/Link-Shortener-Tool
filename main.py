"""
Description:
    Name: Link Shortner
    Tool: A Daily-Use url shorter Tools
    Author: Md SiFaT IsLaM
    GitHub: https://github.com/cyber-programer
    Version: 1.0

Note:
    This Tool is Open Source
    You can Use any Code.
    But consider giving Credit!
"""



import requests as req
import shutil
import sys
import time
from colors import color
from bs4 import BeautifulSoup


columns = shutil.get_terminal_size().columns

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def logo():
    x = color.red+'''
    ░█░░░▀█▀░█▀█░█░█░░░█▀▀░█░█░█▀█░█▀▄░▀█▀░█▀▀░█▀█░█▀▀░█▀▄
    ░█░░░░█░░█░█░█▀▄░░░▀▀█░█▀█░█░█░█▀▄░░█░░█▀▀░█░█░█▀▀░█▀▄
    ░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀
    
    (Author: Md SiFaT IsLaM {root_lovs})
    '''+color.reset
    
    # Calculate the center position for the logo
    center_position = (columns - max(len(line) for line in x.split('\n'))) // 2
    
    # Print each line of the logo centered
    for line in x.split('\n'):
        # print(line.center(columns))
        type_text(line.center(columns))
        print()

    type_text(color.green+'[^] Short any long link:\n'+color.reset)

# logo()

def show_list():
    domains = {
        'is.gd',
        'cutt.ly',
        'v.gd',
        'bitly.ws',
        'xy2.eu',
        'tunyurl.mobi',
        'shorturl.at',
        'sniply',

        }
    print()
    type_text(color.green+'[*] Your Options : \n'+color.reset)
    
    no = 1
    
    for domain in domains:
        print()
        type_text(color.yellow+f'[{no}] {domain}\n'+color.reset)
        no +=1
    
    print()
    type_text(color.green+'[*] chose anynumber : \n'+color.reset)
    usr = input(color.red+'=> '+color.reset)
    print()
    
    user_chonse = list(domains)[int(usr) -1]
    
    return user_chonse
    
    
def main():
    
    try:
        usr = show_list()
    except ValueError:
        type_text(color.red+'[-] Enter correct value\n'+color.reset)
        sys.exit()
    except IndexError:
        type_text(color.red+'[-] Your number is out of range\n'+color.reset)
        sys.exit()
        

    try:
        type_text(color.green+'Enter you URL:\n'+color.reset)
        url = input(color.red+'=>'+color.reset)
        
        if usr ==  'tunyurl.mobi':
            api = f'http://tinyurl.mobi/create.php?url={url}'
            
            try:
                res = req.get(api)
                short_url = res.url.replace('/show','')
                type_text(color.green+f'[+] Short URL: {short_url}\n'+color.reset)  

                 
            except Exception as e:
                print(e)
        
        elif usr ==  'is.gd':
            api = f'https://is.gd/create.php?format=simple&url={url}'
            
            try:
                res = req.get(api)
                type_text(color.green+f'[+] Short URL: {res.text}\n'+color.reset)  
            except Exception as e:
                print(e)
        
        elif usr ==  'cutt.ly':
            api = f'https://cutt.ly/api/api.php?key=af8c6a9bebc3a7415ffe7d7f493c784f45718&short={url}'
            
            try:
                response = req.get(api)
                data = response.json()

                # Check if the request was successful (status 7)
                if data["url"]["status"] == 7:
                    short_link = data["url"]["shortLink"]
                    print(f"Short Link: {short_link}")
                else:
                    print(f"Error: Unable to shorten the link. Status: {data['url']['status']}")
            except requests.RequestException as e:
                print(f"Error: {e}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                
        elif usr ==  'v.gd':
            api = f'https://v.gd/create.php?format=simple&url={url}'
            
            try:
                res = req.get(api)
                type_text(color.green+f'[+] Short URL: {res.text}\n'+color.reset)  
            except Exception as e:
                print(e)
                
                
        elif usr ==  'bitly.ws':
            api = f'http://bitly.ws/create.php?url={url}'
            
            try:
                res = req.get(api)
                short_url = res.url.replace('/show','')
                type_text(color.green+f'[+] Short URL: {short_url}\n'+color.reset)  
            except Exception as e:
                print(e)
                
                
        elif usr ==  'xy2.eu':
            api = f'http://xy2.eu/create.php?url={url}'
            
            try:
                res = req.get(api)
                short_url = res.url.replace('/show','')
                type_text(color.green+f'[+] Short URL: {short_url}\n'+color.reset)  
                
            except Exception as e:
                print(e)
        
        elif usr == 'sniply':
            
            api = "https://snip.ly/pub/snip"
            data = {"url": url, "cta_message": "Sign up and customize the CTA!", "button_url": "https://sniply.io/pricing/"}
            try:
                response = req.post(api, json=data)
            except requests.exceptions.ConnectionError:
                error("net")

            if not (response.status_code == 201) and not (response.status_code == 200):
                error(response.status_code)

            shortUrl = response.json()["snip_url"]
            type_text(color.green+f'[+] Short URL: {shortUrl}\n'+color.reset)
        
        
    
            # type_text(color.green+f'[+] Short URL: {text_input}\n'+color.reset)
            
            
            
            
            
    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    logo()
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        type_text(color.red+'You Stope This Tool \nThanks For Using this Tool\n\nAllah Hafez /^-_-^\ \n\n'+color.reset)