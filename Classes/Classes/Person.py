#3. Write a class Person    - 
    #Have this class have state: name    
    #Have this class have action: legally_change_name()    
    #Have this class have action: introduce_myself()   
    #Create two poeple and have them introduce themselves. Change one of their names. Have them introduce themselves again.

class Person:
    def __init__(self, name):
        self.name = name    

    def introduce_myself(self):
        print("My name is {}".format(self.name))

    def legally_name_change(self, name):
        self.name=name
        print("The name has been changed to {}".format(self.name))


if __name__ == '__main__':
    r=Person("Martin")
    r.introduce_myself()
    r.legally_name_change("Tintin")


    r=Person("Sam")
    r.introduce_myself()
    r.legally_name_change("Sampras")

