"""
#
# File        : q1
# Created     : 29/09/21 8:54 PM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Guessing game
#
"""


if __name__ == '__main__':
    while 1:
        print("Guess the number?")
        number = input()
        if int(number) == 5:
            print("\nYou are right!!! \n")
            break
        else:
            print("\nSorry, would you like to retry?(yes/no) ")
            consent = ""
            while 1:
                consent = input()
                # Handles if user entered invalid input
                if consent != 'yes' and consent != 'no':
                    print("\nPlease enter a valid reply (yes/no): ")
                else:
                    break
            if consent == 'no':
                break
    print("Finished")
