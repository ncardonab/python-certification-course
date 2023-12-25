def read_int(prompt, min, max):
    number = int(input(prompt))
    if number >= min and number <= max:
        return number

    raise Exception('Number is not in range')


try:
    v = read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)
except ValueError:
    print('Please do not enter a string')
except Exception as error:
    print(error)
    print(f'Error: the value is not within permitted range ({min}..{max})')