
raw_input=input("Please enter tuples: ")

#t=tuple(int(x.strip()) for x in raw_input.split(',') if type(x) == 'int' else ''  

t = tuple(i.strip() if type(i)=='int' else type(float) for i in raw_input.split(','))

print(t)