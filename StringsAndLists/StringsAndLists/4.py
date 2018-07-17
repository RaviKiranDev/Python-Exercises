# Get the string
s = input('Please enter a string: ')
r=1
t=''
for char in s:
    if r%2==0:
        #Print the result
        t = t+char.upper()
    else:
        t=t+char.lower()
    r += 1 
print(t)  
