"""
#
# File        : q1
# Created     : 30/09/21 9:36 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Test pass, break & continue
#
"""


if __name__ == '__main__':
    for i in range(10):
        print("{0} inside for".format(i))
        if i == 6:
            print("Inside If")
            pass
        elif i == 7:
            print("Inside Else If")
        print("After if and elif")
    print("Outside the for")
