
#l1= [0, 3, 6, 9, 10, 2, 5] 
#l2= [2, 6, 4, 7, 8, 1, 15]

number1 = (input("Enter comma separated numbers1:"))
number2 = (input("Enter comma separated numbers2:"))

l1=number1.split(',')
l2=number2.split(',')

s1=set(map(int,l1))
s2=set(map(int,l2))

l3= list(set(s1.intersection(s2)))

print(l3)
