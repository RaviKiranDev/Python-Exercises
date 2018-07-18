
s=input("Please enter a string: ")
d=input("Please enter a delimeter: ")

def CountOfWords(s, d=''):
    l1 = s.split(d)
    return len(l1)

print(CountOfWords(s,d))
