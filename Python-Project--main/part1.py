from collections import Counter
from typing import Iterable
import os


def read_file(file_path):
    # words separated by a whitespace in a text file
    with open(file_path, 'r', encoding='ANSI') as f: # encoding ANSI because of the swe_news check note pad
        words = f.read().split()
    return words


def count_unique_words(lst):
    # number of unique words
    unique_words = set() # set builds unordered group of unique elements
    for word in lst:
        unique_words.add(word)
    return f'Number of unique words: {len(unique_words)}'


def top_10_most_frequent(lst):
    #  top 10 most used words with length > 4
    # Counter is a dictionary subclass, it counts and keeps unique elements  
    c = Counter()
    for w in lst:
        if len(w) > 4:
            c[w] += 1
    # Counter allow us to find the frequency 
    dic=dict(c.most_common(10)) # empty dict with most common using counter class
    for d in dic:
        print(d)


def get_previous_functions(file_name):
    # prints unique words and top 10 most used words
    path = os.getcwd() + '\\files_for_part1\\' + file_name
    print(f'\nReading from {file_name}:')
    all_words = read_file(path)
    print(count_unique_words(all_words))
    print("Top 10 most frequent: ")
    print(top_10_most_frequent(all_words))


get_previous_functions('brian_14147_words.txt')
get_previous_functions('swe_news12951518_words.txt')