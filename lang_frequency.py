from collections import Counter
import os
import re


def load_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as text_file:
        text = text_file.read()
    return text


def get_frequent_word_counter(text):
    word_dict = {}
    words = re.findall(r'\w+', text)
    lower_words = [word.lower() for word in words]
    word_counter = Counter(lower_words)
    return word_counter


if __name__ == '__main__':
    filepath = input('Enter file name/path: ')
    text = load_text(filepath)
    word_counter = get_frequent_word_counter(text)
    top_10_words = word_counter.most_common(10)
    print(top_10_words)
