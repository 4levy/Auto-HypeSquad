# -*- coding: utf-8 -*-
import os
from shutil import get_terminal_size
import fade
import yaml
import ctypes
import random
import re
from pathlib import Path 
import time
import sys
import logging
from itertools import cycle
import requests
from colorama import Fore, init
from pypresence import Presence
from threading import Thread
from pystyle import Colors, Colorate, Write, System, Center, Box, Anime, Add


init(autoreset=True)

# value
SOFTWARE_TYPE = "Auto HypeSquad"
STATUS = "Released"
VERSION = "0.0.1"
DEVELOPER_TEAM = "4levy"
INVITE_LINK = "TSdpyMMfrU"
DISCORD_INVITE = f"https://discord.gg/{INVITE_LINK}" 
user32 = ctypes.windll.user32

USER = os.getlogin()
CLIENT_ID = '1051536465470963812'
IMAGE_KEY = [
    "aa",
]

MENU = f"""
         _           __       __       __          
 _    __(_)__  ___ _/ /____ _/ /_____ /a /__ ___ ___
| |/|/ / / _ \/ _ `/ __/ _ `/  '_/ -_) / -_|_-<(_-<
|__,__/_/_//_/\_, /\__/\_,_/_/\_\\__/_/\__/___/___/
             /___/                                 

----- by {DEVELOPER_TEAM} < {VERSION} > .gg/{INVITE_LINK} -----

1. House of Bravery
2. House of Balance
3. House of Brilliance
"""

LOADER = """

---------------+----=--*%=--%=%-----------------=-------=++%=--------------
-----#--------------%--*++----+#---=---=---------+-*-----++++=--#--*+------
-+-=----------------=-=%+----*++#=--=---=-----------------++++++-----=-----
-=-*=-=-----=---------%%+------+@*------=---------------+--+++++@*-=--#+---
-=-==-------=-%-------*++-----%==@---#---=---------=-#---%--+++=+#*--%--=--
---=----------@---=---*+=------=++==--#---=---------=-#--**--+++--+%+--=-+%
---+----------*---=--=*+--------*+===-----=+---------+----#+=-#++--++=+----
--=#-*-----#--+---=--#++--------%#+-=------%#---------+----=+--@++---+%-*-+
=-=--#-----*--=---=--@@+---------=+---=-----@*---------+=---+++-**+----+@=@
+-------------+---=--#@=----------==--==-----@%----------=---#+@--=+*@*+*+=
+-------------%------#*-----------++@@@+=-----@#=---------=--+%++--*++#+#*+
+-------------#------*+-------------++--@#+=-=-#+#--#------=--%*+=+-%=*+---
*-----------#--------*+--------------=---#@%-++=@#@--@=--=--#--@+=-+--=----
=--=------*-#--------*+---------------=+---==-#--@@+--=---%--@+-@+---*-@--%
===*=-----%-*-==-----#=-----------=%*-=@%---*#=@--%%%@--@--*+-=@-@+--------
--*%=-----@-+@------#+@@@@@@@@@@@@@*=---===*=-=#+--%%=*=-*+--+--@-#+----==%
==#%=-----@-++=#-=*-@=@@@@@@@@@@@@@@@@@@@+%=-%@*===-+#++#-=@--%@-@==+-----%
===+=-====#=+=%@--+-+=###++@+@@#@@@@@*@@@@@@@*-=*@=@--+%++@=%@-*+@=@-*----@
=%===-====+-+@@=@-----%++++++@@@@@@@@#*@@@@@@%@==-#@---=*+++@#@%-#=@#=@----
=====-====@@+@@%+-----%++++++@@@@@@@@#@@@@@*%@@@@=--==@-@#++--@=*==---@=---
======-==*@@+=*=%@--=+%-------@@@%@@+%@@-@@@@@@@@@+---*=*==@=----*%-+----%-
==#*=#-===@%+===+@====@-------@@@@@#@@@@@@@@@@@+--=*----++=%@=-----*=------
-+@++@-===@@====+#@===*==------@#=#@*@@@@@@*@@@=-----------@+=#-----+------
=+@++@-=++%@@==%=+@@=++=======-=@@@%=@@@%@@--@#-----------------------#----
+-@+++-+++*%++++=%*=+=+==========%%-@@#@@@+@%=--@----------------------%-=-
+=*+++=+++=%=%++%+##===#=#=========+%%@###-@@=--------------------------@#-
#=-#++@=+++%=+++++@*+++#%#=*@======*#%%==========---------=-===============
=+++++@-+++@=+@++@+%++++#+++++==+====+=+===================================
+@+-++#-+++@+++++++*+*+++%++++++++++++=+===================================
+=@+-++#+++@*==%++@+%=%#++@+++++*++*+++++++==============*#*=============+=
++=#@-+@-++*@=++@++@+*=%@++@++#++++*++++*++++=+=+=+=====##*+*===+====+=++++
@++=*==@-+++@%=++*++#+*=*+++@+#++*++++*++++++++++++++++##++##++++++++++++++
#+++=%==#=++@@*+++++*+*@=++@+@+++#++++*+++++++++++++++%#++%%*++++++++++++++
+@++%=+=@=++@+@=++#++%+#%@#+%+#*+*++++++++++++++++++++#**#%**++++++++++++++
**+++@=+++=++#+@+++%*+@+*%#*++#**+++++++++++++++++++++*#*#**#++++++++++++++
++@++%*-+%=++@++*+++@#+*+*@@++++++@+++++++++++++++++++++++***++++++++++++++
=%+@++@++++=+@++*+*+*@%+**#@@@+++++++++++++++++++++++++++++++++++++++++++++
==+%+++%**==++%#+**@+*%%++@@@@@+++++++@==+=+**#*#%%%@@+++++++++++++++++++++
==@+@++%+#@+==@*%+*%@+=+@++@@@@@@+*%=====+++**##%%@@%@@@@*+++++++++++++++++
+++#+@++@+#+++#%*@+#@=#@%%*+@@@@@=====+=+*+*%%**+@@@%@@@@@@@+++++#@@@#*++++
+++++*@++@+@+++@%%%++@*@+%+%+@@@======++===+=%++%#%%@@@%@@@@@+++*@@@@@@@@@@

"""


def load_config():
    try:
        with open('config.yml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            if config and "TOKEN" in config:
                tokens = [token.strip() for token in config["TOKEN"].split('\n') if token.strip()]
                config["TOKENS"] = tokens 
        return config
    except FileNotFoundError:
        Console.Log("ERROR", "RED", "config.yml file not found!")
        return None
    except yaml.YAMLError as e:
        Console.Log("ERROR", "RED", f"Error parsing YAML file: {e}")
        return None
    
class Console:
    
    @staticmethod
    def Log(info, color, mess):        
        print(f"[{Fore.MAGENTA}MIYAKO{Fore.RESET}] - {info} - {getattr(Fore, color)}{mess}")

    @staticmethod
    def Clear():
        os.system("cls" if os.name == "nt" else "clear")

# RPC
RPC = Presence(CLIENT_ID)

def get_all_discord_usernames():
    directories = [
        os.getenv('APPDATA') + "\\discord",
        os.getenv('APPDATA') + "\\discordptb",
        os.getenv('APPDATA') + "\\discordcanary",
        os.getenv('LOCALAPPDATA') + "\\discord"
    ]
    
    usernames = set()
    username_pattern = r'"username"\s*:\s*"([^"]+)"'

    for directory in directories:
        try:
            if not os.path.exists(directory):
                continue
                
            local_storage_path = Path(directory) / "Local Storage" / "leveldb"
            if not local_storage_path.exists():
                continue

            for file_path in local_storage_path.glob("*.ldb"):
                try:
                    for encoding in ['utf-8', 'latin-1']:
                        try:
                            with open(file_path, "r", encoding=encoding) as f:
                                content = f.read()
                                matches = re.finditer(username_pattern, content)
                                for match in matches:
                                    username = match.group(1).strip()
                                    if 2 <= len(username) <= 32 and username != "Unknown":
                                        usernames.add(username)
                            break
                        except UnicodeDecodeError:
                            continue
                except Exception as e:
                    Console.Log("ERROR", "RED", f"Error reading file {file_path}: {e}")
                    continue

        except Exception as e:
            Console.Log("ERROR", "RED", f"Error accessing directory {directory}: {e}")
            continue

    if not usernames:
        Console.Log("WARN", "YELLOW", "No Discord usernames found, using system username")
        return [os.getlogin()]
        
    return list(usernames)

def initialize_rpc():
    try:
        RPC = Presence(CLIENT_ID)
        RPC.connect()
        start_time = int(time.time())
        def update_rpc():
            while True:
                usernames = get_all_discord_usernames()
                username_display = ", ".join(usernames) if usernames != ["Unknown"] else "Unknown"
                for image in IMAGE_KEY:
                    try:
                        RPC.update(
                            state=f"Dev | {DEVELOPER_TEAM}",
                            details=f"{SOFTWARE_TYPE} | {STATUS} | Users > {username_display}",
                            large_image=image,
                            large_text=f"Version: {VERSION}",
                            start=start_time
                        )
                    except Exception as e:
                        print(f"[RPC Error] {e}")
                    time.sleep(10)
        Thread(target=update_rpc, daemon=True).start()
    except Exception as e:
        print(f"\nDiscord RPC Error: {e}\n")

# End

class DotLoader:
    def __init__(self, desc="Initializing RPC : ", end="★ Initialization Complete!", timeout=0.3):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False
        self._thread = Thread(target=self._animate, daemon=True)

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc}{c}", end="", flush=True)
            time.sleep(self.timeout)

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        Console.Log("INFO", "BLUE", self.end)
        
def send_hypesquad_request(token: str, house_id: int):
    url = "https://discord.com/api/v9/hypesquad/online"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    payload = {"house_id": house_id}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 204:
        Console.Log("SUCCESS", "GREEN", f"Successfully joined HypeSquad house ID {house_id}")
        return True
    elif response.status_code == 429:
        retry_after = response.json().get('retry_after', 5)
        Console.Log("WARN", "YELLOW", f"Rate limited! Waiting {retry_after} seconds...")
        time.sleep(retry_after + 0.5)  
        return send_hypesquad_request(token, house_id)
    else:
        Console.Log("ERROR", "RED", f"Failed! Status code: {response.status_code} | Response: {response.text}")
        return False


def Main():
    os.system(f'mode con: cols=155 lines=40 & title [{SOFTWARE_TYPE}] - MainRR- {STATUS}')
    Console.Clear()

    
    print(f"{Colorate.Horizontal(Colors.blue_to_purple, MENU)}")
    
    config = load_config()
    if not config or "TOKEN" not in config:
        Console.Log("ERROR", "RED", "Missing token in config.")
        return

    tokens = config.get("TOKENS", [])
    if not tokens:
        Console.Log("ERROR", "RED", "No valid tokens found in config.")
        return
    
    print("\n")
    Console.Log("INFO", "BLUE", f"Loaded {len(tokens)} tokens")
    choice = input(Colorate.Horizontal(Colors.blue_to_red, '\n[?] Choose house (1-3) > '))
    
    house_id = None
    if choice == "1":
        house_id = 1
    elif choice == "2":
        house_id = 2
    elif choice == "3":
        house_id = 3
    else:
        Console.Log("ERROR", "RED", "Invalid choice!")
        return

    success_count = 0
    fail_count = 0
    
    for i, token in enumerate(tokens, 1):
        Console.Log("INFO", "BLUE", f"Processing token {i}/{len(tokens)}")
        try:
            response = send_hypesquad_request(token, house_id)
            if response:
                success_count += 1
            else:
                fail_count += 1
            if i < len(tokens):
                time.sleep(1)
        except Exception as e:
            Console.Log("ERROR", "RED", f"Error with token {i}: {str(e)}")
            fail_count += 1
    
    Console.Log("INFO", "BLUE", f"Operation completed: {success_count} successful, {fail_count} failed")
    
    input(": ")
    Main()

def Loader():
    Console.Clear()
    os.system(f'mode con: cols=155 lines=40 & title [{SOFTWARE_TYPE}] - LoaderRR- {STATUS}')
    
    Console.Log("INFO", "MAGENTA", LOADER)
    Console.Log("INFO", "BLUE", f"Hello, {USER}!")
    
    loader = DotLoader()
    loader.start()
    initialize_rpc()
    time.sleep(2)
    loader.stop()
    
    Main()

if __name__ == "__main__":
    try:
        Loader()
    except KeyboardInterrupt:
        print("\n")
        Console.Log("INFO", "RED", "Exiting gracefully...")
        sys.exit(0)