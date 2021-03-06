import time
import os
from os import environ as env
import schedule

from dotenv import load_dotenv
load_dotenv()

import datetime

token = env['token']
pattern = [3, 3, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 3]
pattern_counter = 0
pattern_length = len(pattern)
general_counter = 0

def color_density(weight):
    print('### Colorify ###')
    if weight == 0:
        print('No commit today')
    for w in range(weight):
        print('Commit {number}'.format(number=w))
        # append new line to logs file
        with open('logs/painting.txt', 'a') as file:
            file.write(str(w) + '\n')
            os.system("git add * && git commit -m \"{}\" && git push https://{}@github.com/gitpainter/painter".format(str(w), token))
            time.sleep(5)


def paint_pattern(shade):
    global pattern
    color_density(pattern[shade])

def paint_my_git():
    global pattern_counter
    global pattern_length
    if pattern_counter < pattern_length:
        paint_pattern(pattern_counter)
        pattern_counter = pattern_counter + 1
        return
    elif pattern_counter == pattern_length:
        pattern_counter = 0 # repeat pattern
        return

schedule.every().day.at("17:13").do(paint_my_git)
#schedule.every(10).seconds.do(paint_my_git)


while True:
    schedule.run_pending()
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)