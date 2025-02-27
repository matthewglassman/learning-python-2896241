#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file named textfile.txt for writing and create it if it doesn't exist using w+
    #myfile = open("textfile.txt", "w+")
    
    # Open the file for appending text to the end
    #myfile = open("textfile.txt", "a+")

    # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some new text\n")
    
    # # close the file when done
    # myfile.close()

    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    #Check to see if the mode is correctly set to read and if so store the contents in a variable and print them to screen.
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)
    #Could use readlines() method to read each lines as a separate item in an array as well.
if __name__ == "__main__":
    main()
