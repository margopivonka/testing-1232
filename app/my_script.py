def enlarge(i):
    return i * 100

#need to remove the following from global scope in order to import other things from this script to the test one
#my_number  = float(input("Please input a number: "))
#n = enlarge(my_number)
#
#print("ENLARGING THE NUMBER: ", n)


if __name__ == "__main__":
    #only run this if invoked by command line, not imported by another file
    my_number  = float(input("Please input a number: "))
    n = enlarge(my_number)

    print("ENLARGING THE NUMBER: ", n)
    