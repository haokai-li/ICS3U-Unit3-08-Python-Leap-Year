#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program calculate leap year


def main():
    # This function calculate leap year

    # input
    user_string = input("Please enter the year: ")
    print("")

    # process
    try:
        user_year = int(user_string)
        if user_year % 4 != 0:
            # output
            print("It is a common year.")
        else:
            if user_year % 100 != 0:
                # output
                print("It is a leap year.")
            else:
                if user_year % 400 != 0:
                    # output
                    print("It is a common year.")
                else:
                    # output
                    print("It is a leap year.")
    except Exception:
        # output
        print("{} is not a valid input.".format(user_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
