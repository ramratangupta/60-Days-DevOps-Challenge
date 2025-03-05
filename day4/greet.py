
import sys

def greet():
    if len(sys.argv)>1:
        name = sys.argv[1]
        if name == None or name=="":
            print(sys.argv[0]+" <name>")
    else:
        print("Enter Name : ",end=" ")
        name = input()
    print("Hello "+name+" !!")
if __name__ == "__main__":
    greet()