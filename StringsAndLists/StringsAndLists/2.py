# Get the string
s = input('Please enter a string: ')

i=len(s)

# Convert the string to upper or lowercase (as appropriate), and print it
if s[i-1]=='!':
    print(s.upper())
else:
    print(s.lower())