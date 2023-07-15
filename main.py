import pyautogui
import keyboard
import time
import random

from itertools import combinations

from config import *

a = False

str_keys = ""
for i in keys:
	str_keys += i



def spam():
	pyautogui.click()
	#time.sleep(random.uniform(0.0001, 0.01))


keyboard.add_hotkey(active_button, spam)
hot_key = []
for item in range(len(keys) + 1):
	if item >= 1:
		data = list(combinations(str_keys, item))
		for e in data:
			q = ""
			for event in e:
				event = event.replace("S", "Shift")
				event = event.replace("C", "Ctrl")
				event = event.replace(" ", "Space")

				q += f" + {event}"

			keyboard.add_hotkey(f"{active_button}{q}", spam)

while True:
	keyboard.wait()