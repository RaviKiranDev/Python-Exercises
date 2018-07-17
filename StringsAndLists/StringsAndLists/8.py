

number1 = int(input("Enter a divisor:")) #4
number2 = int(input("Enter a number:")) #20

l=[]

for i in range(1,number2):
    if i%number1==0:
        l.append(i)
print(l)