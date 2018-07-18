
d = dict()

while True:
    user_data = input("Please enter a coordinate-word pair in the format (x, y, word): ")
    if user_data!='':
        t1 = tuple(user_data.split(','))
        d[t1[:2]] = t1[2]
    else:
        break


while True:
    user_data_lookup = input("Please enter a coordinate to look up: ")
    if user_data_lookup!='':        
        t2 = tuple(user_data_lookup.split(','))                
    else:
        break

if user_data_lookup != 'q':
    print(d.get(t2, 'Coordinate not found'))

