#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
#Functions start with the word def followed by the function name and parameters in parentheses and then a colon
def func1():
    print("I am a function") # this is the body of the function.


# TODO: function that takes parameters
def func2 (arg1, arg2): 
    print(arg1, " ", arg2)

# TODO: function that returns a value
def cube(x):
    return x * x  * x #will multiply x times itself 3 times and then return that value to function call.


# TODO: function with default value for an parameter


# TODO: function with variable number of parameters


#Function execution examples (wrong and right)
func1() #prints I am a function from direct function call
print(func1()) #prints I am a function  and also prints out the return value of NONE 
print(func1) #Function definition is being printed where the object resides in memory

func2(10, 20)
print(func2(10, 20))

print(cube(3))