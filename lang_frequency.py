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


def get_most_frequent_words(low_words):
    word_counter = Counter(low_words)
    top_10_dict = word_counter.most_common(10)
    top_10_list = [i[0] for i in top_10_dict]
    return top_10_list


if __name__ == '__main__':
    filepath = input('Enter file name/path: ')
    text = load_text(filepath)
    low_words = get_lowered_words(text)
    top_10_words = get_most_frequent_words(low_words)
    print(top_10_words)
