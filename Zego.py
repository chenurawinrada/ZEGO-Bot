VERSION = "3.0"

import os
import sys
import time
import datetime
import openai
import pyttsx3
import hashlib
import maskpass
import requests
import urllib
import colorama
import random
import json
from packaging import version
from colorama import Fore, init, Style
from urllib.request import urlopen
init()
g = Fore.GREEN
m = Fore.MAGENTA
y = Fore.YELLOW
c = Fore.CYAN
w = Fore.WHITE
B = Style.BRIGHT

colors = [g, m, y, c, w]

# Talk function
def talk(text):
    engine = pyttsx3.init()
    if check_connection(timeout=1):
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[2].id)
    else:
        pass
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def check_for_update():
    if check_for_updates():
        print("Updates available!")
        print("Go to https://github.com/chenurawinrada/ZEGO-Bot and update!")
        talk("Updates available!")
    else:
        os.system('cls')

def check_for_update_u():
    if check_for_updates():
        print("Updates available!")
        print("Go to https://github.com/chenurawinrada/ZEGO-Bot and update!")
        talk("Updates available!")
    else:
        update_talks = ["I'm up to date.", "I am up to date sir.", "There is no available updates sir."]
        update_random = random.choice(update_talks)
        print(update_random)
        talk(update_random)

def AIChat():
    try:
        with open('key.txt', 'r') as key_:
            _key = key_.read()
            key_.close()
        if _key == '':
            k = input("Enter the openai api key to key.txt and rerun the command: ")
            main()
        else:
            with open('key.txt', 'r') as key_:
                _key = key_.read()
                key_.close()
            

        openai.api_key = _key
        def generate_text(prompt):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=1024,
                n=1,
                stop=None,
            )

            message = response.choices[0].text.strip()
            return message

        print(f"{y}If you want to hear the text, then use {w}'-t'{y}at the start of the sentence{g}, Type 'exit' to return to zego.")
        while True:
            prompt = input("(ChatGPT)>> ")
            if '-t' in prompt:
                prompt = prompt.replace('-t', '')
                try:
                    if prompt != "exit" and prompt != "cls":
                        message = generate_text(prompt)
                        message = message + '\n'
                        talk(message)
                    elif prompt == 'cls':
                        os.system('cls')
                    else:
                        main()
                except KeyboardInterrupt:
                    main()
            else:
                try:
                    if prompt != "exit" and prompt != "cls":
                        message = generate_text(prompt)
                        message = message + '\n'
                        print(message)
                    elif prompt == 'cls':
                        os.system('cls')
                    else:
                        main()
                except KeyboardInterrupt:
                    main()
    except Exception as e:
        print(str(e))
def check_for_updates():
    try:
        print("Checking for updates")
        if check_connection(timeout=1):
            url = 'https://raw.githubusercontent.com/chenurawinrada/ZEGO-Bot/main/metadata.json'
            # url = 'https://github.com/chenurawinrada/ZEGO-Bot/blob/main/metadata.json'
            rqt = requests.get(url, timeout=5)
            meta_sc = rqt.status_code
            if meta_sc == 200:
                metadata = rqt.text
                json_data = json.loads(metadata)
                gh_version = json_data['version']
                if version.parse(gh_version) > version.parse(VERSION):
                    return True
                else:
                    return False
        else:
            os.system('cls')
            pass
    except json.decoder.JSONDecodeError as e:
        print(str(e))
        sys.exit(0)
# Animated logo
def logo():
    WIDTH = 50

    message = "ZEGO".upper()

    printedMessage = ["", "", "", "", ""]

    characters = {" ": [" ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " "],
                  "Z": ["▒███████▒",
                        "▒ ▒ ▒ ▄▀░",
                        "░ ▒ ▄▀▒░ ",
                        "  ▄▀▒   ░",
                        "▒███████▒",
                        "░▒▒ ▓░▒░▒",
                        "░░▒ ▒ ░ ▒",
                        "░ ░ ░ ░ ░",
                        "  ░ ░    ",
                        "░"],
                  "E": ["▓█████  ",
                        "▓█   ▀  ",
                        "▒███   ▒",
                        "▒▓█  ▄ ░",
                        "░▒████▒░",
                        "░░ ▒░ ░ ",
                        " ░ ░  ░ ",
                        "   ░   ░",
                        "   ░  ░ ",
                        ""],
                  "G": [" ▄████  ",
                        "██▒ ▀█▒▒",
                        "██░▄▄▄░▒",
                        "▓█  ██▓▒",
                        "▒▓███▀▒░",
                        "░▒   ▒ ░",
                        " ░   ░  ",
                        " ░   ░ ░",
                        "     ░  "],
                  "O": [" █████",
                        "██▒  ██▒",
                        "██░  ██▒",
                        "██   ██░",
                        " ████▓▒░",
                        " ▒░▒░▒░",
                        " ░ ▒ ▒░",
                        " ░ ░ ▒",
                        "   ░ ░"]}

    for row in range(5):
        for char in message:
            printedMessage[row] += (str(characters[char][row]) + " ")
    offset = WIDTH
    counttime = 0
    while counttime != 50:
        counttime = counttime + 1
        time.sleep(0.01)
        os.system('cls')
        for row in range(5):
            blow = random.choice(colors)
            print(blow+ B + " " * offset + printedMessage[row][max(1, offset*-1):WIDTH-offset
                                                     ])
        offset -= 1
        if offset <= ((len(message)+2)*6)*-1:
            offset = WIDTH
    time.sleep(0.9)
    print("********ZEGO THE FUTER OF AI********")

def bannar():
    print(f"""{c}

                    ▒███████▒▓█████   ▄████  ▒█████
                    ▒ ▒ ▒ ▄▀░▓█   ▀  ██▒ ▀█▒▒██▒  ██▒
                    ░ ▒ ▄▀▒░ ▒███   ▒██░▄▄▄░▒██░  ██▒
                      ▄▀▒   ░▒▓█  ▄ ░▓█  ██▓▒██   ██░
                    ▒███████▒░▒████▒░▒▓███▀▒░ ████▓▒░
                    ░▒▒ ▓░▒░▒░░ ▒░ ░ ░▒   ▒ ░ ▒░▒░▒░
                    ░░▒ ▒ ░ ▒ ░ ░  ░  ░   ░   ░ ▒ ▒░
                    ░ ░ ░ ░ ░   ░   ░ ░   ░ ░ ░ ░ ▒
                      ░ ░       ░  ░      ░     ░ ░
                    ░{c}VERSION {VERSION}
{g}""")

# Greeting
def greet():
    current_time = time.strptime(time.ctime(time.time())).tm_hour
    try:
        with open("user.txt", "r") as u:
            li = u.read()
            u.close()
        if current_time < 12:
            talk("Good morning" + li)
        elif current_time == 12:
            talk("Good noon" + li)
        elif current_time > 12 and current_time < 18:
            talk("Good afternoon" + li)
        elif current_time >= 18:
            talk("Good evening" + li)
    except ValueError:
        pass

# Start all the functions
def start():
    os.system('title ZEGO')
    os.system('cls')
    print(f'{w}Starting....{g}')
    time.sleep(1)
    os.system('cls')
    logo()
    data()
    greet()
    os.system('cls')
    bannar()
    sign()

# Try to find the database if not, automatically created
def data():
    try:
        with open('user.txt', 'r') as u:
            u.close()
    except FileNotFoundError:
        print("Creating databases....")
        user = open('user.txt', 'w')
        user.close()
    try:
        with open('passwd.txt', 'r') as pwd:
            pwd.close()
    except FileNotFoundError:
        pwd = open('passwd.txt', 'w')
        pwd.close()
    try:
        with open('key.txt', 'r') as key:
            key.close()
    except FileNotFoundError:
        key = open('key.txt', 'w')
        key.close()

# Signining in
def sign():
    with open('passwd.txt', 'r') as pwd:
        line = pwd.read()
        pwd.close()

    if line == '':
        talk("""Welcome to the future of artificial inteligence.
        First, let me introduce myself.
        My name is Zego.
        And I'm a fully functional console bot.
        I can help you with your day-today works.
        So, Let's get started!
        Create a profile to begin.""")
        pwd = maskpass.askpass(prompt="Creat a password: ", mask="#")
        conf_pwd = maskpass.askpass(prompt="Confirm the password: ", mask="#")
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("passwd.txt", "w") as f:
                f.write(hash1)
                f.close()
            with open('user.txt', 'w') as u:
                user = input("How may I call you?: ")
                u.write(user)
                print("Login completed!")
                talk("Profile created sucessfully.")
            time.sleep(2)
            os.system('cls')
            check_for_update()
            bannar()
            commands()
            main()
        else:
            print("Sorry, Password was wrong!\n Try again!")
            time.sleep(2)
            os.system('cls')
            bannar()
            sign()
    else:
        entpd = maskpass.askpass(prompt="Enter your password: ", mask="#")
        enc1 = entpd.encode()
        hash2 = hashlib.md5(enc1).hexdigest()
        if line == hash2:
            talk("Access granted!")
            os.system('cls')
            time.sleep(2)
            check_for_update()
            bannar()
            commands()
            main()
        else:
            talk("Access denied!")
            talk("Wrong password! Try again!")
            time.sleep(1)
            os.system('cls')
            bannar()
            sign()

# Built in commands
def commands():
    lines = [
    '\n    *********************************\n',
    '        COMMANDS TO USE\n\n',
    'x   Terminate the robot',
    'R   Restart the bot',
    'u   Check for updates',
    'h   Give this help',
    's   Search in wiki',
    'a   AI Chat (ChatGPT)',
    'g   Play a game',
    'C   Check the network connection',
    'c   Clear my memory\n',
    '*********************************\n'
    ]
    for line in lines:
        time.sleep(0.1)
        print(f"    {c}{line}")

# Games
def games():
    names_array = ['Ashley', 'Angus', 'Doctor Octopus', 'Doctor Strange',
                   'Tiger', 'Alian', 'Roku', 'Spinix', 'Iron Man', 'Slitherin',
                   'Grefindo', 'Juliana', 'Spider man', 'Lusi', 'Anne'
                   ]
    talk("What about this?")
    name = (random.choice(names_array))
    talk(name)
    print(f"{m}{name}")
    talk("Do you like it?")
    an = input(f"{w}Do you like it?(y/n):{m} ")
    if an == 'y':
        games()
    elif an == 'n':
        talk("Do you want to continue?")
        d = input(f"{w}Do you want to continue?(y/n):{m}")
        if d == 'y':
            games()
        elif d == 'n':
            main()
        else:
            print("Enter correct one!")
            main()
    elif an == 'q':
        main()
    else:
        print("Tell me y or n!")
        games()

# This function is use to check the network connection
def check_connection(timeout=1):
    try:
        urllib.request.urlopen('https://www.google.com', timeout=1)
        return True
    except Exception:
        return False

# Use in command(to check the conection)
def network():
    if check_connection(timeout=1):
        talk("Connection is in good state.")
    else:
        talk("""Connection error!
        Make sure that you are connected to the internet!""")

# Search in wiki
def search():
    if check_connection(timeout=1):
        import wikipedia
        try:
            b = input(f"{c}Type here to search:{w} ")
            d = input(f"{c}How many lines do you want?:{w} ")
            info = wikipedia.summary(b, d)
            print(f"{m}Here are the results:{w}\n\n{info}\n")
        except Exception:
            talk("Sorry, URLError")
            main()
    else:
        print("Check the connection and try again!")
        main()

# Main function(Bot)



def main():
    with open('user.txt', 'r') as u:
        li = u.read()
        u.close()
    says = [
    f'{li}, are you sure about this? Because, if you do this my memory will be deleted.',
    f"{li}, You cant clear my memory!"
    ]
    try:
        while True:
            a = input(f"{g}(ZeGo)>>{w} ")
            if a == 'x':
                talk("have a nice day")
                sys.exit(0)
            elif a == 'h':
                commands()
            elif a == 's':
                search()
            elif a == 'g':
                print("Enter 'q' to quit")
                games()
            elif a == 'C':
                network()
            elif a == 'R':
                talk("Restarting")
                start()
            elif a == 'a':
                AIChat()
            elif a == 'u':
                if check_connection(timeout=1):
                    check_for_update_u()
                else:
                    print("Connect to a network first!")
                    talk(f'{li}, There is no network connection at this moment!')
            elif a == 'c':
                talk(random.choice(says))
                b = input('Do you want to procceed?(y/n): ')
                if b == 'y':
                    os.remove('user.txt')
                    os.remove('passwd.txt')
                    talk('All memory data cleared')
                    talk('Restarting')
                    start()
                elif b == 'n':
                    talk(f'Thanks {li}')
                else:
                    pass
            else:
                print(f"{c}Use 'h' for help")
    except Exception:
        sys.exit(0)

if __name__ == '__main__':
    start()
