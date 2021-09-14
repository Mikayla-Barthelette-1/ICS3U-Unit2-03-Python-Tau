#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program finds the circumference of a circle using tau

import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("The circumference is: {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
