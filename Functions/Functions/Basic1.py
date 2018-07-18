
n=int(input("Please enter a number: "))

def factorial(n):
    if n<0:
        return 'Please pass in a positive number'
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))