"""
#
# File        : q3
# Created     : 30/09/21 10:24 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Total digits, up case & down case letters
#
"""


if __name__ == '__main__':
    text = input()
    digit = 0
    upCase = 0
    downCase = 0
    for element in text:
        if element.isdigit():
            digit += 1
        elif element.isupper():
            upCase += 1
        elif element.islower():
            downCase += 1
    print("Total digit: {0}".format(digit))
    print("Total up case: {0}".format(upCase))
    print("Total down case: {0}".format(downCase))
