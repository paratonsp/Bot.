import psutil
import time

while True:
    print("----------------")
    print(psutil.cpu_percent())
    print(psutil.virtual_memory().percent)
    print("----------------")
    time.sleep(1)
