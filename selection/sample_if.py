"""
#
# File        : sample_if.py
# Created     : 27/09/21 10:08 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : If example
#
"""


if __name__ == '__main__':
    grade = input("Enter a grade: ")
    grade = int(grade)

    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print("You have earned a Distinction!")
    elif grade >= 60:
        print("You have earned a M.1.!")
    elif grade >= 50:
        print("You have earned a M.2.!")
    elif grade >= 40:
        print("You passed!")
    else:
        print("Please try again")
