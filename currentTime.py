import time

currentTime = time.localtime(time.time())

print(f"hours:{currentTime.tm_hour}, min:{currentTime.tm_min} sec:{currentTime.tm_sec}")