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