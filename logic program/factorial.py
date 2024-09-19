def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)
    
def factorialTrialZero(number):
    
    # fac = factorial(number)
    # if(fac%10 == 0):
    #     fac = fac / 10
    
    #------------------or ---------------------
    
    #  5! = 5 * 4 * 3 * 2 * 1 = 120 == 1 zero
    #  6! = 6 * 5 * 4 * 3 * 2 * 1 = 480 == 1 zero
    # 100! = 100 * 99 * .... *26 * 5 * 5 * 24 *23 ... *1
    
        # Let’s take an example with number = 100:

        # First Iteration:

        # i = 5
        # number // i = 100 // 5 = 20
        # Add 20 to the cumulative count (Z-axis).
        # Second Iteration:

        # i = 25 (next power of 5)
        # number // i = 100 // 25 = 4
        # Add 4 to the cumulative count (Z-axis).
        # Third Iteration:

        # i = 125 (next power of 5)
        # number // i = 100 // 125 = 0 (no need to continue as this is zero)
        # The cumulative count remains as is.
        # In 3D, you would see:

        # A vertical bar at X = 5, Y = 20, and Z = 20.
        # Another vertical bar at X = 25, Y = 4, and Z = 24 (20 + 4).
        # No bar at X = 125 because number // i is zero.
            
    count = 0
    i = 5
    while(number//i !=0):
        count += int(number/i)
        i = i*5
    return count
        
number = int(input("Enter number for factorial:"))
# print(f"Facrotial is: {factorial(number)}")
print(factorialTrialZero(number))   