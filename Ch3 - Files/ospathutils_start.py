#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print ("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", path.isfile("textfile.txt")) #Checks to see if item is a file and prints this line as True or False
    print("Items is a directory", path.isdir("textfile.txt")) #Checks to see if item is a directory and prints this line as True or False
    
    # Work with file paths
    print("Item's path:", path.realpath("textfile.txt")) #Prints full path and filename
    print("Item's path and name:", path.split(path.realpath("textfile.txt"))) #creates path and separately the filename as a tuple

    
    # Get the modification time

    
    # Calculate how long ago the item was modified

  
if __name__ == "__main__":
    main()
