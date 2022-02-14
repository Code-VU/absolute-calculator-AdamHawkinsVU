def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    
    try:
        set_num = int(in_num)
        if set_num <= 21:
            smaller_abs_diff = abs(set_num - 21)
            print ("Result:",smaller_abs_diff)
        elif set_num > 21:
            larger_abs_diff = abs(2*(set_num - 21))
            print ("Result:",larger_abs_diff)
    except:
        print ("Error: Please input a Number.")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateAbsolute()