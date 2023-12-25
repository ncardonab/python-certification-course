import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

filename = input("Enter the filename: ")

cwd = os.path.dirname(__file__)
print(cwd)
filepath = f'{cwd}/{filename}.txt'
filepath_hist = f'{cwd}/{filename}.hist'

try:
    stream = open(file=filepath, mode='r', encoding='utf-8')

    just_latin_letters = filter(lambda letter : letter.isalpha(), stream.read())

    lower_case = map(str.lower, just_latin_letters )

    letters_histogram = Counter(lower_case)

    sorted_by_value = sorted(letters_histogram.items(), key=lambda x : x[1], reverse=True)

    letters_histogram = {key: value for key, value in sorted_by_value}

    counts = letters_histogram.values()
    letters = letters_histogram.keys()

    for key, value in letters_histogram.items():
        print(f'{str( key )}->{str( value )}')

    bar_x_locations = np.arange(len(counts))
    plt.bar(bar_x_locations, counts, align = 'center')
    plt.xticks(bar_x_locations, letters)
    plt.grid()
    plt.show()

    stream.close()

    stream = open(file=filepath_hist, mode='w', encoding='utf-8')

    for key, value in letters_histogram.items():
        stream.write(f'{key} -> {value}\n')

    stream.close()
except Exception as e:
    print(e)