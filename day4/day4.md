* **Challenge 1** : Create a Python program that accepts a user’s name as input and prints a greeting message.
code greet.py
```python
import sys
def greet():
    if len(sys.argv)>1:
        name = sys.argv[1]
        if name == None or name=="":
            print(sys.argv[0]+" <name>")
    else:
        print("Enter Name: ",end=" : ")
        name = input()
    print("Hello "+name+" !!")
greet()

```   
run above as

`python3 greet.py`

or 

`python3 greet.py Ram`

* **Challenge 2** : Write a script that reads a text file and counts the number of words in it.

code countwords.py
```python
import sys
import os

def wordCount():
    if len(sys.argv)>1:
        fileName = sys.argv[1]
    else:
        print("Input filename ")
        fileName = input()
    if fileName == None or fileName =="":
        print("Filename is empty")        
    elif os.path.exists(fileName) and os.path.isfile(fileName):
        try:
            with open(fileName) as file:
                content = file.read()
                words = content.split(" ")
                print(f"Total words in file {fileName} is : {len(words)}")
        except Exception as e:
            print(e)
        finally:
            file.close()
    else:
        print(fileName+" does not exists or it is a folder")
wordCount()
```
run above as

`python3 greet.py`

or 

`python3 greet.py day4.md`

* **Challenge 3** : Create a Python script that generates a random password of 12 characters.
code my_random.py
```python
import uuid
print(uuid.uuid4().hex[:12])

```
Run as below

`python3 my_random.py`

* **Challenge 4** : Implement a Python program that checks if a number is prime.
code checkPrime.py
```python
import sys
def checkPrime(num):
    num = int(num)
    if(num<0):
        print(f"{num} is not a valid postive numer")
        sys.exit()
    elif num==1:
        print(f"Number 1 is prime")
    else:
        isPrime = True
        for i in range(2,num+1):
            if num % i==0 and num!=i:
                isPrime = False
                break
        if isPrime:
            print(f"Number {num} is prime!!")
        else:
            print(f"Number {num} is Not prime!!")


print("Please input number to check it is prime or not",end=" : ")
number = input()
checkPrime(number)
```
```
ramratan@ramratan-pc:~/60-Days-DevOps-Challenge/day4$ python3 checkPrime.py
Please input number to check it is prime or not : 37
Number 37 is prime!!
ramratan@ramratan-pc:~/60-Days-DevOps-Challenge/day4$ python3 checkPrime.py
Please input number to check it is prime or not : 51
Number 51 is Not prime!!
ramratan@ramratan-pc:~/60-Days-DevOps-Challenge/day4$ python3 checkPrime.py
Please input number to check it is prime or not : 97
Number 97 is prime!!
ramratan@ramratan-pc:~/60-Days-DevOps-Challenge/day4$ 

```
* **Challenge 5** : Write a script that reads a list of server names from a file and pings each one.
code ping_servers.py
```python
import os
import subprocess
def pingServers(fileName):
    try:
        with open(fileName) as file:
            for line in file:
                line = line.strip().replace("http://","")
                if line !="":
                    print(f"Ping for {line}")
                    r = subprocess.run(["ping","-c", "5", "-w", "3", line])
                    print(r)
    
    except Exception as e:
        print(e)
    finally:
        file.close()

    pass
print("Please input filename which contains list of server names: ",end="")
fileName = input()
if fileName=="":
    print("Filename is empty")
else:
    if os.path.exists(fileName) and os.path.isfile(fileName):
        pingServers(fileName)
    else:
        print(f"{fileName} dose not exists or it is dir")

```
* **Challenge 6** : Use the requests module to fetch and display data from a public API (e.g., JSONPlaceholder).
code fetch_api.py
```python
import requests
try:
    data = requests.get("https://jsonplaceholder.typicode.com/users")
    if data.status_code==200:
        apiData = data.json()
        for row in apiData:
            print(f"{row['id']}\t{row['name']}")
except Exception as e:
    print(e)
```
* **Challenge 7** : Automate a simple task using Python (e.g., renaming multiple files in a directory).
code rename_files.py
mkdir /tmp/test
touch /tmp/test/ram1.txt
touch /tmp/test/ramratan.txt
touch /tmp/test/ram1gupta.txt
```python
from pathlib import Path
import os
def rename_files(folder):
    path = Path(folder)
    for item in path.iterdir():
        if os.path.isfile(item):
            try:
                old_name = str(item)
                print(f"Renaming file {item} to .md")
                os.rename(old_name,old_name.replace(".txt",".md"))
            except Exception as e:
                print(e)
                

dir = input("Enter dir path for all files to renamed by removing space to _ : ")
if dir=="":
    print("DIR path is empty")
    exit()
if not os.path.exists(dir):
    print(f"{dir} DIR path is not found")
    exit()
if os.path.isfile(dir):
    print(f"{dir} is a file")
    exit()
rename_files(dir)
```
```
python3 rename_files.py
Enter dir path for all files to renamed by removing space to _ : /tmp/test
Renaming file /tmp/test/ramratan.txt to .md
Renaming file /tmp/test/ram 1 ratan.txt to .md
Renaming file /tmp/test/ram1.txt to .md
Renaming file /tmp/test/ram 1.txt to .md
Renaming file /tmp/test/ram1gupta.txt to .md
Renaming file /tmp/test/ram 1 gupta.txt to .md
Renaming file /tmp/test/ram to .md
```
* **Challenge 8** : Create a Python script that monitors CPU and memory usage every 5 seconds.
code monitor_cpu_ram.py
```python
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
```
chmod 777 monitor_cpu_ram.py
./monitor_cpu_ram.py

* **Challenge 9** : Write a Python program that creates a user in Linux using subprocess and verifies the creation.
code create_user.py