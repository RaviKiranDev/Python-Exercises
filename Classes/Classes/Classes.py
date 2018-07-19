
class Horse:
    def __init__(self, name, color, age, owner, worth=5000):
        self.name=name
        self.color=color
        self.age=age
        self.owner=owner
        self.worth=worth
    
    def set_name(self, name):
        self.name=name
    
    def set_lifespan(self, years):
        self.lifespan=years
        print("The lifespan is {}".format(years))

    def set_color(self, color):
        self.color=color
        print("The new color is {}".format(color))

    def set_weight(self, weight):
        self.weight=weight
        print("The weight is {}".format(weight))


hr = Horse("San", "White", 8, "Robert")
hr.set_color("Brown")
hr.set_lifespan(25)
hr.set_weight(55)

print("name: "+ hr.name) 
print("color: "+ hr.color) 
print("owner: " + hr.owner)


    

        


