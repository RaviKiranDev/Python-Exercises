
i=1
total=0

while i<=50:
    total += i
    if total > 100:
        print(i)
        print("The sum exceeded the max value of 100.")
        break;
    i += 1