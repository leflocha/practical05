# TODO: Refactor all of this source code so that it fully adheres
# to the source code standard for the Python programming language

#!/usr/bin/env python
# pylint: disable=C0114 # missing-module-docstring
import sys, re, operator, string

#
# The functions
#
def read_file(path_to_file):
    """
    Takes a path to a file and returns the entire
    contents of the file as a string
    """
    with open(path_to_file) as f:
        data = f.read()
    return data

def filter_chars_and_normalize(str_data):
    """
    Takes a string and returns a copy with all non-alphanumeric
    chars replaced by white space
    """
    pattern = re.compile(r'[\W_]+')
    return pattern.sub(' ', str_data).lower()

def scan(str_data):
    """
    Takes a string and scans for words, returning
    a list of words.
    """
    return str_data.split()

def remove_stop_words(word_list):
    """
    Takes a list of words and returns a copy with all stop
    words removed
    """
    with open('../stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
    """
    Takes a list of words and returns a dictionary associating
    words with frequencies of occurrence
    """
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs

def sort(word_freq):
    """
    Takes a dictionary of words and their frequencies
    and returns a list of pairs where the entries are
    sorted by frequency
    """
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

def print_all(word_freqs):
    """
    Takes a list of pairs where the entries are sorted by frequency and print them recursively.
    """
    if(len(word_freqs) > 0):
        print(word_freqs[0][0], ' - ', word_freqs[0][1])
        print_all(word_freqs[1:]);

#
# The main function
#

if __name__ == "__main__":
    str_data = read_file(sys.argv[1])
    str_data = filter_chars_and_normalize(str_data)
    word_list = scan(str_data)
    word_list = remove_stop_words(word_list)
    word_freq = frequencies(word_list)
    word_freqs = sort(word_freq)

    for tf in word_freqs[0:25]:
        print(tf[0], "-", tf[1])
