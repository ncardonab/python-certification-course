import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

filename = input("Enter the filename: ")

cwd = os.path.dirname(__file__)
print(cwd)
filepath = cwd + '/' + filename

try:
    stream = open(file=filepath, mode='r', encoding='utf-8')
    just_latin_letters = filter(lambda letter : letter.isalpha(), stream.read())
    alphabetical_ordered_letters = sorted(map(str.lower, just_latin_letters ))
    letters_histogram = Counter(alphabetical_ordered_letters)
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
except Exception as e:
    print(e)