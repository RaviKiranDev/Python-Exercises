
numbers = input("Enter numbers separated by dashes(-): ")

l1 = list(map(int,numbers.split(' - ')))

dict1 = {x : x **2 for x in l1}

print(dict1)