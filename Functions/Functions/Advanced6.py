s=input("Please enter a list of strings: ")
n=input("Inputted letter: ")

def StringSearch(s, n):
    l1 = list(s.split())

    l2=[s for s in l1 if n in s]

    return l2

print(StringSearch(s,n))
