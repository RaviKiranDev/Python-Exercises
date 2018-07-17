x=int(input("Enter a number"))

if x <=9:
    print("This is a good number.")
elif x > 9 and x <=99:
    if x%3==0:
        print("This is a best number.")
    else:
        print("This is a better number.")
else:
    print("Horrible number.")