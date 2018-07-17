
x = input("Enter a string:")
y = input("Enter a letter to count the number of occurances:")

count=0

for char in x:
    if char.lower()==y.lower():
        count += 1
print(count)