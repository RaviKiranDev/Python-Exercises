numbers = input("Enter numbers separated by commas: ")

l1= list(map(int,numbers.split(',')))

l2 = l1[::2]
l3 = l1[1::2]

zipped = list(tuple(zip(l2,l3)))

print(zipped)