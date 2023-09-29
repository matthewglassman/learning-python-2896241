#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 1000, 100   

    # conditional flow uses if, elif, else

    # if x < y:  #Compare x above is less than y  
    #     result = "x is less than y"
    # #What is they are the same?
    # elif x == y:
    #     result = "x and y are the same"
    # #Now lets put in an else statement to handle when X is greater than Y.
    # else: 
    #     result = "x is greater than y"
    # print(result)

    # conditional statements let you use "a if C else b"
    
    #Same as above but in one line and minus the ELIF.
    # result = "x is less than y" if x < y else "x is greater or equal to y"
    # print(result)

    # match-case makes it easy to compare multiple values
    value = "fifteen"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":  #Handles multiple possible values so 3 or 4
            result = (3,4)
        case _: #handles anything else
            result = -1
    print(result)

if __name__ == "__main__":
    main()
