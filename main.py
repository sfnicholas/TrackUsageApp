import win32gui
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import atexit
import ast

def exit_handler():
    with open('record.txt', 'w') as f:
        f.write(f"{process_time}")
    
def open_handler():
    with open('record.txt') as f:
        return f.readline()

records = open_handler()
process_time = ast.literal_eval(records)

timestamp = {}
atexit.register(exit_handler) #handle this function when exit program
while True:
    #get app
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    
    #current time express in seconds
    timestamp[current_app] = int(time.time()) 
    time.sleep(1)
    
    if current_app not in process_time.keys():
        process_time[current_app] = 0 #starting time
    process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    print(process_time)

