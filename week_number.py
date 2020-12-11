#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program is for week number


def main():
    # this function is for week number

    # input
    week_day = input("Enter a week day number: ")

    # process & output
    try:
        week_day_int = int(week_day)
        if week_day_int <= 5 and week_day_int >= 1:
            if week_day_int == 1:
                print("Monday")
            elif week_day_int == 2:
                print("Tuesday")
            elif week_day_int == 3:
                print("Wednesday")
            elif week_day_int == 4:
                print("Thursday")
            else:
                print("Friday")
        else:
            print("It is not a weekday")
    except Exception:
        print("It is not a integer")


if __name__ == "__main__":
    main()
