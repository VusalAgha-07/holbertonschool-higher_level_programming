#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
