"""
#
# File        : q2
# Created     : 30/09/21 10:05 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Count even and odd numbers
#
"""


if __name__ == '__main__':
    maxNumber = input("enter the maximum number: ")
    evenNumber = 0
    oddNumber = 0
    for i in range(1, int(maxNumber)+1):
        if (i % 2) == 0:
            evenNumber += 1
        else:
            oddNumber += 1
    print("Total {0} even numbers".format(evenNumber))
    print("Total {0} odd numbers".format(oddNumber))
