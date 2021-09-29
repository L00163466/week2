"""
#
# File        : loops.py
# Created     : 27/09/21 10:42 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Loops example
#
"""


if __name__ == '__main__':
    text = ""
    while 1:
        print("Enter name")
        unane = input()
        if unane == "joe":
            break
        print("\nSorry, try again! \n")
    print("Finished")

    # max = 5
    # counter = 0
    # total = 0
    # while counter <= max:
    #     total += 9.99
    #     counter += 1
    # print("The final amount is: {0:5.2f}".format(total))

    # for i in range(1, 10):
    #     if i == 6:
    #         print("Found")
    #         break
    #     print("Not Yet")
    # print("It was found at {}.".format(i))

    # for i in range(1, 20):
    #     if (i % 5) == 0:
    #         print("Buzz")
    #     print("bizz")

    from string import ascii_lowercase

    # manifesto = """ Lorem ipsum gammot
    #             Lorem ipsum gammot"""
    # for ch in manifesto:
    #     print(ch, end="")
    # for ch in ascii_lowercase:
    #     print(ch)
    # for i in range(10):
    #     print(i)
    #
    # print("\n")
    #
    # for i in range(10, 5, -1):
    #     print(i)

    # for i in range(0, 12, 3):
    #     print(i)

