#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
#To use shell functionality need to import the following:
import shutil


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):  #to make sure the file exists
        # get the path to the file in the current directory
        src = path.realpath("textfilie.txt")
        # let's make a backup copy by appending "bak" to the name
        #first lets create the destination of the path and file by concatenating the path and the file that we want to copy
        destination = src + ".bak"

        #Next we will use the copy function of the shutil module to copy the source to the destination
        shutil.copy(src,destination)

        # rename the original file
        
        # now put things into a ZIP archive

        # more fine-grained control over ZIP files

      
if __name__ == "__main__":
    main()
