#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

#Lets build an application that manages vehicles

#By convention all of the methods in a class take the reference to the object as the first parameter.
class Vehicle():
    def __init__(self,bodystyle): #function/method is what Python calls when the object has been created and it is time to initialize the object's data
        self.bodystyle = bodystyle #define a property on the class that will take what is equal to the bodystyle parameter that gets passed in.
        
