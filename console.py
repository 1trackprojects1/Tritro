# -*- coding: utf-8 -*-
'''
████████╗██████╗ ██╗████████╗██████╗  ██████╗   Made By @trackic (telegram)
╚══██╔══╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔═══██╗  DO NOT message me for support, open an issue on github.
   ██║   ██████╔╝██║   ██║   ██████╔╝██║   ██║  I will not provide any guarantee of you getting a vaild code.
   ██║   ██╔══██╗██║   ██║   ██╔══██╗██║   ██║  
   ██║   ██║  ██║██║   ██║   ██║  ██║╚██████╔╝  I am not responsible for anything you do with the information
   ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   or the code provided in this github repo.
'''
import random, json, requests, string
from progress.bar   import IncrementalBar

class settings:
    runs = 5

class internaldata:
    avg = []

def check(code, proxy='http://7ujn87ku:4JST9cRFG6LfzOcI@proxy.proxy-cheap.com:31112'):
    session = requests.session()
    session.proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        r = session.get('https://discord.com/api/v8/entitlements/gift-codes/' + code, timeout=2)
        data = json.loads(r.text)
        try:
            if data['code'] == 10038:
                bar.next()
            elif data['code'] == code:
                print '\n[$] checked valid - ' + str(code)
                bar.next()
        except KeyError:
            print r.text
    except:
        bar.next()

def generatecode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(16))

print '''
████████╗██████╗ ██╗████████╗██████╗  ██████╗   There are about 10,000,000,000,000,000 combinations
╚══██╔══╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔═══██╗  of a 16 character long alphanumeric string. You
   ██║   ██████╔╝██║   ██║   ██████╔╝██║   ██║  have a 1 in a sextillion chance of getting a valid
   ██║   ██╔══██╗██║   ██║   ██╔══██╗██║   ██║  nitro code everytime you generate & check.
   ██║   ██║  ██║██║   ██║   ██║  ██║╚██████╔╝  
   ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   v1.1.3 by @trackic (telegram)
'''

bar = IncrementalBar('Initializing:', max=settings.runs, suffix='%(percent).1f%% - [ %(elapsed)ds / %(eta)ds ]')
for i in range(0, settings.runs):
    check(generatecode())
bar.finish()