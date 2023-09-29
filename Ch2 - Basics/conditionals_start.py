#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 1000, 100   #Causes and error because X will no longer be less than Y and so variable 'result' never gets created and thus print can't print anything.

    # conditional flow uses if, elif, else

    if x < y:  #Compare x above is less than y  
        result = "x is less than y"
    print(result)

    # conditional statements let you use "a if C else b"

    # match-case makes it easy to compare multiple values
    value = "one"

if __name__ == "__main__":
    main()
