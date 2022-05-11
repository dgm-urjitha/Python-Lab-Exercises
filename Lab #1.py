#!/usr/bin/env python3
#Lab exercise-1 Lakshmi Urjitha Dhadigam
# display a welcome message
print("The Miles Per Gallon program")
print()
# get input from the user
for  i in range(3):
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_gallon = float(input("Enter cost per gallon: "))
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
    # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon: ", mpg)
        tgc =round(gallons_used * cost_gallon,2)
        print("Total Gas Cost:  ", tgc)
        cpm =round(tgc / miles_driven,2)
        print("Cost Per Mile:  ", cpm)    
    
    

print()
print("Bye!")



