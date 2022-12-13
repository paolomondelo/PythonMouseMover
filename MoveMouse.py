import pyautogui
import time

# Set the time to stop moving the cursor (in 24-hour format)
stop_hour = 18
stop_minute = 30

while True:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min

    # Check if the current time is past the stop time
    if current_hour > stop_hour or (current_hour == stop_hour and current_minute >= stop_minute):
        break

    pyautogui.moveRel(100, 100)
    time.sleep(180)
