# mr rat library

import random
import socket
from urllib.request import Request, urlopen
from flask import Flask, render_template

class game():
    def wordsearch():
        words = ['juicy']
        print('''
        A | I | Y | T | O 
        J | B | C | U | N 
        K | J | I | H | J 
        H | U | U | M | I 
        Y | Z | J | X | S 
        ''')
        print('Enter the first word: ')
        word = input('>>> ')
        if not word.lower() in words:
            print(f'Word {word} is not correct.')
        else:
            print(f'Word {word} is correct!')

    def hangman(hangman_words):
        word = random.choice(hangman_words)
        wrong = 0
        win = False
        found = []
        while wrong == 0 and win == False:
            l = input('Enter a letter\n>>> ')
            if l in word and not l in found:
                print(f'Found {l}!')
                found.append(l)
            else:
                print(f'Letter {l} either already found or not in word.')
                wrong += 1
        if len(word) == len(found):
            win = True
            print('You win.')
        if wrong >= 10:
            print('You lose.')

    def all_games():
        print('''
        MrRat.game.wordsearch()
        Wordsearch
        
        MrRat.game.hangman()
        Hangman
        ''')

class hacking():
    def port_scanner():
        sock = socket.socket()
        port = input('Enter the number of ports to scan: ')
        target_ip = input('Enter the target IP address: ')

        for i in range(port):
            try:
                sock.settimeout(0.5)
                sock.connect((target_ip, port))
                print(f'[+] Port {i} is open.')
            except:
                print(f'[-] Port {i} is closed.')

    def phishing_site():
        link = input('[+] Enter link to copy: ')
        try:
            with urlopen(Request(link)) as response:
                f = open('phishing.html', 'a')
                f.write(response)
                f.close()
            app = Flask(__name__)

            @app.route('/')
            def phishingpage():
                render_template('phishing.html')

            if __name__ == '__main__':
                app.run()
        except '404' in response:
            print('[-] Unable to access site.')
        except:
            print('[-] Failed to copy.')