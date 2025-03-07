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
