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
def power(num, x=1): #x=1 is a default value in case 2nd argument isn't given.
    result = 1;
    #Takes a number and raises it to a power and the loop will run whatever number x is in the 2nd argument
    for i in range(x):
        result = result * num
    return result

# TODO: function with variable number of parameters
def multi_add(*args):  # the * means I can pass in a variable number of arguments and named arguments/parameters come first.
    result = 0
    for x in args:
        result = result + x
    return result

#Function execution examples (wrong and right)
# func1() #prints I am a function from direct function call
# print(func1()) #prints I am a function  and also prints out the return value of NONE 
# print(func1) #Function definition is being printed where the object resides in memory

# func2(10, 20)
# print(func2(10, 20))

# print(cube(3))

# print(power(2)) #will take the default x=1
# print(power(2,3)) #will use 3 for x
# print(power(x=3, num=2)) #python knows what to do since the parameters are named in the function call.

print(multi_add(4,5,10,4))