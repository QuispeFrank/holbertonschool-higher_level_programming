#!/usr/bin/python3
""" Text indentation module """


def text_indentation(text):
    """
        prints a text with 2 new lines after each
        of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in ['.', ':', '?']:
        text = (c + '\n\n').join([sbs.strip() for sbs in text.split(c)])
    print(text, end='')
