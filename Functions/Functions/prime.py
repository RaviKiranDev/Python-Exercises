
n=int(input("Please enter a numberrr: "))

def CheckForPrime(n):
    p=0
    if n<=0:
        return 'Please pass in a positive number'
    else:
        for i in range(1,n+1):
            if n%i==0:
                p += 1
            continue
    if p==2:
        return 'The number you inputted is a prime'
    else:
        return 'The number you inputted is not a prime'

print(CheckForPrime(n))