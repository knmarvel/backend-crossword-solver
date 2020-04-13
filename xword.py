#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "knmarvel"

import re

# YOUR HELPER FUNCTION GOES HERE
def change_to_regex(test_word):
    re_str = "^"
    for letter in test_word:
        if letter == " ":
            re_str += "."
        else:
            re_str += f'({letter})'
    return re_str + "$"


def find_matches(re_str, words):
    matches = []
    for word in words:
        if re.findall(re_str, word):
            matches.append(word)
    return matches


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    re_str = change_to_regex(test_word)
    print("\n".join(find_matches(re_str, words)))

if __name__ == '__main__':
    main()
