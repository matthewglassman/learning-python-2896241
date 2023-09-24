#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

def main():
    print("Hello World!")
    name = input("What is your name?")
    print("Nice to meet you", name)


#This tells Python to look for the function above
#This Python function should run as a main function
#Also it tells Python that this is a standalone program
#And not a module or chunk of code to be exported
if __name__ == "__main__":
    main()