
s=input("Please enter a string: ")
d=input("Please enter a delimeter: ")

def CountOfWords(s, d=''):
    l1 = s.split(d)
    l2=[]

    for item in l1:
        l2.append(len(item))

    return l2

print(CountOfWords(s,d))