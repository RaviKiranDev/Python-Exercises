
s = set()
while True:
    inp= input("Enter a word to add to the vocabulary: ")
    if inp!='' and inp != 'q':
        s.add(inp)        
    else:
        break
if inp!='q':
    string  = ',' .join(s)
    print (string)


