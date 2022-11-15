import random
import pyautogui as pg
import time
animal = ('Dog', 'Monkey', 'Cow', 'Buffalow', 'Elephant', 'Donkey', 'Cat',)
time.sleep(10)
for i in range (100):
 a = random.choice(animal)
 pg.write('You Are a' + a)
 pg.press('enter')
