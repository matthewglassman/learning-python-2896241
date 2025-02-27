#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
#x = 10 / 0
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#     x = 10 /0
# except:
#     print("Well that didn't work. You can't divide by 0")


# TODO: You can also catch specific exceptions

#the following can cause multiple errors (divide by 0, not a number, etc). Can write multiple exceptions
try:
    answer = input("What should I divide 10 by?")
    num = int(answer) #take input and convert to an integer and store in num variable
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by 0")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally: #Contains code that will always run. Can be used to clean up resources that were allocated like open files.
    print("This code always runs")
