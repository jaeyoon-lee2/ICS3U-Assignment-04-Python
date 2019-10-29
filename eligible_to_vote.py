#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program determine eligibility to vote


def main():
    # this function determine eligibility to vote

    # input
    integer_as_string = input("Enter your age (integer): ")

    # process
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
