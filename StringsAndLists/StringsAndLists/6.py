
number1 = int(input("Enter a number:"))
number2 = int(input("Enter a divisor:"))

l=[]

for number2 in range(1,number1+1):
    if number1%number2==0:
        l.append(number2)
print(l)