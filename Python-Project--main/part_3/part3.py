import operator
import HashSet as hashSet
import BstMap as bstMap
import os


def read_file(file_path):
    # words separated by a whitespace in a text file
    with open(file_path, 'r', encoding='ANSI') as file: 
            all_words=file.read().split()
    return all_words


def count_unique_words(lst):
    # number of unique words
    unique_words = hashSet.HashSet()
    unique_words.init()
    for each_word in lst:
        unique_words.add(each_word)
    result = f'Number of unique words: {unique_words.get_size()}\n'
    result += f'Hashset buckets list size: {unique_words.bucket_list_size()}\n'
    result += f'Hashset Maximum bucket size: {unique_words.max_bucket_size()}\n'
    result += f'Hashset zero bucket ratio: {round(unique_words.zero_bucket_ratio(),2)}\n'
    return result


def top_10_most_frequent(lst):
    # top 10 most used words with length greater than 4
    all_words=bstMap.BstMap()
    for each_word in lst:
        if len(each_word) > 4:
            found=all_words.get(each_word)
            if found is not None:
                add_node=found + 1
                all_words.put(each_word, add_node)
            else:
                all_words.put(each_word,1)
    words_list=all_words.as_list()
    sorted_words_list = sorted(words_list, key=operator.itemgetter(1), reverse=True)
    i=0
    result=""
    while i < 10 and i < len(sorted_words_list):
            result += f'{i+1} - "{sorted_words_list[i][0]}" used {sorted_words_list[i][1]} times.\n'
            i += 1
    result += f'\nBstMap - Number of nodes: {all_words.count_nodes()}\n'
    result += f'\nBstMap - Maximum of depth: {all_words.max_depth()}\n'
    result += f'\nBstMap - Number of leafs: {all_words.count_leafs()}\n'  

    return result
    

def get_previous_functions(file_name):
    # prints unique words + top 10 most used words, number of nodes, max depth and number of leafs
    path = os.getcwd() + "\\part_3\\" +  file_name
    print(f'\nReading from {file_name}:')
    all_words = read_file(path)
    print(count_unique_words(all_words))
    print("Top 10 most frequent: ")
    print(top_10_most_frequent(all_words))


get_previous_functions('brian_words.txt')
get_previous_functions('swe_news_words.txt')