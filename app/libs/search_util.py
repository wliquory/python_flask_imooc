#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_isbn_or_key(word):
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9的组合，含有一些'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and (len(short_word) == 10) and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key


def get_isbn(data_dict):
    isbn = data_dict.get('isbn')
    if not isbn:
        isbn = data_dict.get('isbn13')
        if not isbn:
            isbn = data_dict.get('isbn10')
    return isbn
