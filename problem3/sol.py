from math import sqrt

def largestPrimeFacotr(num):
    for i in range(int(sqrt(num)), 0, -1):
        if num % i == 0 and checkPrime(i):
            return i

def checkPrime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True

print(largestPrimeFacotr(600851475143))