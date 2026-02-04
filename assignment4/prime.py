import math as ma

n = int(input())

def prime_number(n:int)->bool:
    if(n < 2):
        return 0
    else:
        for i in range(2, round(ma.sqrt(n)) + 1):
            if(n % i == 0):
                return 0
    return 1

if(prime_number(n)):
    print("this is prime number")
else:
    print("this is not prime number")
