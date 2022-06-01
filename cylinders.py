#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program calculates volume of a cylinder using multiple parameters.

import math


def cylinder_volume(height, radius):
    # this function calculates volume of a cylinder

    # process
    volume = (math.pi * (radius**2)) * height

    return volume


def main():
    # this function gets input, calls a function, gives output
    print("This program calculates the volume of a cylinder using radius and height.")
    print("")

    # input
    radius_string = input("Enter a radius (mm): ")
    height_string = input("Enter a height (mm): ")

    try:
        height_value = float(height_string)
        radius_value = float(radius_string)
        # call function
        volume = round(cylinder_volume(height_value, radius_value), 2)

        # output
        print("\nThe volume of this cylinder is {} mm².".format(volume))

    except Exception:
        print("\nYour values are invalid. Please Re-Run.")

    print("\nDone.")


if __name__ == "__main__":
    main()
