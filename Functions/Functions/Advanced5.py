
s=input("Please enter a list of numbers: ")
d=int(input("Please enter a divisor: "))

def Divisors(s, d):
    l1 = list(map(int,s.split(',')))

    l2=[]

    for num in l1:
        if num%d==0:
            l2.append('yes')
        else:
            l2.append('no')

    return l2

print(Divisors(s,d))