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