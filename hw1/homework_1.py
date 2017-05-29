# Name:
# Section: 
# Date:
# homework_1.py

##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here



def display():
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('-----------')
    print('   |   |')


display()


print "********** Exercise 1.3 **********"


a = '   |   |'
b = '-----------'


def show():
    print a
    print b
    print a
    print b
    print a

show()


 
# Hint - how many different variables will you need? - Ans 2


print "********** Exercise 1.4 **********"


def ui():
    f_name = raw_input('Enter your first name: ')
    l_name = raw_input('Enter your last name: ')
    print('Enter your D.O.B:')
    mo = raw_input("Month: ")
    day = raw_input("Day: ")
    year = raw_input("Year: ")
    print f_name, l_name, "was born on " + mo, day, year


ui()


