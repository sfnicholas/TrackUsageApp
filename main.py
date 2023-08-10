import win32gui
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import atexit
import ast
from pynput.mouse import Listener

#clock section
clock = [0]

def on_click(x,y,button,pressed):
    clock[0] = 0

def on_move(x,y):
    clock[0] = 0

def on_scroll(x,y,dx,dy):
    clock[0] = 0

def exit_handler():
    with open('record.txt', 'w') as f:
        f.write(f"{process_time}")

# record part
def open_handler():
    with open('record.txt') as f:
        return f.readline()

# main program

records = open_handler()
process_time = ast.literal_eval(records)
timestamp = {}
atexit.register(exit_handler) #handle this function when exit program

listener = Listener(
    on_click=on_click, on_move=on_move, on_scroll=on_scroll)
listener.start()

while True:
    #get app
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    
    #current time express in seconds
    timestamp[current_app] = int(time.time()) 

    if current_app not in process_time.keys():
        process_time[current_app] = 0 #starting time

    time.sleep(1)
    clock[0] += 1
    
    if clock[0] < 5:
        process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    
    print(process_time)

