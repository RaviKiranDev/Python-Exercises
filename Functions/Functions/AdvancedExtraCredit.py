
#raw_input=input("Please enter tuples: ")

#t=tuple(int(x.strip()) for x in raw_input.split(',') if type(x) == 'int' else ''  

#t = tuple(i.strip() if type(i)=='int' else type(float) for i in raw_input.split(','))

#print(t)


# Part 2  - Extra Credit 1 & 2
def cal_credit(lst, value):
    result = 0   
    sorted_lst = sorted(lst)
    for inc,per in sorted_lst:
        if value > inc:        
            result = result + (inc * per)        
            value -= inc    
        elif value > 0:        
            result = result + (value * per)        
            value -= inc    
    return result

print(cal_credit([(50000, 0.08), (100000, 0.10), (150000, 0.15)], 70000))