# Scenario
# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.

# Your task is to write a program which:

# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.
# Test your code using the data we've provided.

# Test data
# Sample input:
# 19991229

# Sample output:
# 6

# Sample input:
# 20000101

# Sample output:
# 4

try:
    birthday = input('Enter your birthday date: ')
    sum_of_digits = 0

    while len(str(birthday)) > 1:
        sum_of_digits = 0
        for digit in birthday:
            sum_of_digits += int( digit )
        birthday = str(sum_of_digits)

    print(sum_of_digits)

except KeyboardInterrupt:
    print('Hey!!! why would you close the program so suddenly?')