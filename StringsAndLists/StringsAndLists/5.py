
number = int(input("Enter a number:"))

l=[]

for i in range(0,number):
    if i%2==0:
        l.append(i)
print(l)