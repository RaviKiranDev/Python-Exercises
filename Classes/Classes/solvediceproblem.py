import random

bag = [4, 6, 6, 8, 8, 8, 8, 10, 10, 12, 20, 20, 20]

tot_list = []

roll_again = "yes"
       
print("pull out 3 dice from the bag at randon and set them aside: ")
    
   
while len(bag)>10:
    bag.remove(random.choice(list(bag)))
    print("The dice that were put aside: ", bag)

    #print(random.choice(listt))
    #print(random.randint(min, max))

    #roll_again = input("Roll the dices again?")