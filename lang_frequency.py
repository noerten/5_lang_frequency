from collections import Counter
import os
import re


def load_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as text_file:
        text = ''
        for line in text_file:
            text = text + line
    return text


def get_lowered_words(text):
    words = re.findall(r'\w+', text)
    lower_words = [word.lower() for word in words]
    return lower_words


def get_most_frequent_words(low_words, number_of_words):
    word_counter = Counter(low_words)
    top_dict = word_counter.most_common(number_of_words)
    top_list = [i[0] for i in top_dict]
    return top_list


if __name__ == '__main__':
    filepath = input('Enter file name/path: ')
    number_of_words = int(input('Enter number of most frequent words: '))
    text = load_text(filepath)
    low_words = get_lowered_words(text)
    top_n_words = get_most_frequent_words(low_words, number_of_words)
    print(top_n_words)
