#!/usr/bin/python3
import psutil
import time
import datetime

def monitorCPURam():
    try:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().used / (1024 **3)
        print(f"{datetime.datetime.now()}\t{cpu}\t{mem}")
        time.sleep(5)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Timestamp\t\t\tCPU\tRAM")
    while(True):
        monitorCPURam()