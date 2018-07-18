
n=int(input("Please enter a numberrr: "))

def ReturnAllPrimes(n):
    p=0
    if n<=0:
        return 'Please pass in a positive number'
    else:
        for i in range(1,n+1):
            p=0
            for j in range(1,i+1):
                if i%j==0:
                    p += 1                
            if p==2:
                print(i)                   

ReturnAllPrimes(n)