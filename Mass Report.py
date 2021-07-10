import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f" Dippe Report Tool For Discord ")

print(f"""
{b+Fore.WHITE}
 _ .-') _              _ (`-.    _ (`-.    ('-.         _  .-')     ('-.     _ (`-.              _  .-')   .-') _    
( (  OO) )            ( (OO  )  ( (OO  ) _(  OO)       ( \( -O )  _(  OO)   ( (OO  )            ( \( -O ) (  OO) )   
 \     .'_   ,-.-')  _.`     \ _.`     \(,------.       ,------. (,------. _.`     \ .-'),-----. ,------. /     '._  
 ,`'--..._)  |  |OO)(__...--''(__...--'' |  .---'       |   /`. ' |  .---'(__...--''( OO'  .-.  '|   /`. '|'--...__) 
 |  |  \  '  |  |  \ |  /  | | |  /  | | |  |           |  /  | | |  |     |  /  | |/   |  | |  ||  /  | |'--.  .--' 
 |  |   ' |  |  |(_/ |  |_.' | |  |_.' |(|  '--.        |  |_.' |(|  '--.  |  |_.' |\_) |  |\|  ||  |_.' |   |  |    
 |  |   / : ,|  |_.' |  .___.' |  .___.' |  .--'        |  .  '.' |  .--'  |  .___.'  \ |  | |  ||  .  '.'   |  |    
 |  '--'  /(_|  |    |  |      |  |      |  `---.       |  |\  \  |  `---. |  |        `'  '-'  '|  |\  \    |  |    
 `-------'   `--'    `--'      `--'      `------'       `--' '--' `------' `--'          `-----' `--' '--'   `--'    

 
{b+Fore.WHITE} x > {Fore.RESET}Options

{b+Fore.WHITE} {1} > {Fore.RESET}illegal Content {b+Fore.WHITE}
{b+Fore.WHITE} {2} > {Fore.RESET}Harrassment {b+Fore.WHITE} 
{b+Fore.WHITE} {3} > {Fore.RESET}Spam or Phishing Links {b+Fore.WHITE} 
{b+Fore.WHITE} {4} > {Fore.RESET}Self harm {b+Fore.WHITE} 
{b+Fore.WHITE} {5} > {Fore.RESET}NSFW Content {b+Fore.WHITE} 
""")

token = input(f"{b+Fore.MAGENTA} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.WHITE} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.MAGENTA} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.MAGENTA} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.MAGENTA} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.MAGENTA} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v9/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.WHITE} > Sent Report {b+Fore.MAGENTA}::{Fore.WHITE} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"Report Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.WHITE} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.WHITE} > Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()
