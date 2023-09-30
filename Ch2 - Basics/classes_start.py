#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

#Lets build an application that manages vehicles

#By convention all of the methods in a class take the reference to the object as the first parameter.
class Vehicle():
    def __init__(self,bodystyle): #function/method is what Python calls when the object has been created and it is time to initialize the object's data
        self.bodystyle = bodystyle #define a property on the class that will take what is equal to the bodystyle parameter that gets passed in.

#Now we can create other classes from the base class of Vehicle

class Car(Vehicle):  #The item in the parantheses here is saying that Class Car inherits from Class Vehicle
    def __init__(self, enginetype):
        super().__init__("Car") #Keyword super initializes the super class (in this case Vehicle) and call it's init method and the bodystyle parameter ("Car")
        # Now lets set some other properties for the Class Car
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

#Now lets create a class of Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

#Now lets create/instantiate a couple of cars and a motorcyle
#To do this we use the Class name along with the parameters of the init function/method

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)