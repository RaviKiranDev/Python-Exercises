s=input("Please enter a list of strings: ")
n=input("Inputted letter: ")

def StringSearchIndex(s, n):
    l1 = list(s.split())

    l2=[i for i, s in enumerate(l1) if n in s]

    return l2

print(StringSearchIndex(s,n))

