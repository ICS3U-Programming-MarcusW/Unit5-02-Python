#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Mov 25 2022
# This program calculates the area of a triangle using several functions


def calculate_area(height, base):
    # get the height and base from main input

    # calculate the area of the triangle with the input
    area = (height * base) / 2

    # output the calculated area
    print("The area is {0} cm²".format(area))


def main():
    # this function gets the height and base from the user

    # get the input from the user input
    height_from_user_string = input("Enter the height of a rectangle (cm): ")
    base_from_user_string = input("Enter the base of a rectangle (cm): ")
    print("")

    try:
        # converts the height and base to floats
        height_from_user_float = float(height_from_user_string)
        base_from_user_float = float(base_from_user_string)
        # makes sure input is greater than 0
        if base_from_user_float > 0 and height_from_user_float > 0:
            # call the function to calculate the area
            calculate_area(height_from_user_float, base_from_user_float)
        else:
            # tell the user the inputs can't be negative or zero
            print("The base and height must be greater than 0.")
    # checks if the number is a string
    except Exception:
        print("Invalid data entered! Only numbers can be accepted!")


if __name__ == "__main__":
    main()
