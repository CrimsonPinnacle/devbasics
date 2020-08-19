#!/usr/bin/python

import os
import string
import sys

from random import choices
from colorama import init, Fore, Back

"""
.. module:: random_text_v2
:platform: Unix, Windows
:synopsis: Example script demonstrating the use of log levels in Python

.. moduleauthor:: Toddy Mladenov <toddysm@gmail.com>
"""

def gen_random_string(length = 10):
    """Generates a random string with the specified lenght. The string is made
    of letters only.

    :param length: The length of the string to generate. Default is 10
    :type length: int
    :returns: string - The random string
    """
    word = ''.join(choices(string.ascii_letters, k=length))
    return word

def gen_line(line_length = 10, word_length = 10):
    """Generates a single line with the specified number of words that consist
    of random letters.

    :param line_length: The length of the line in words. Default is 10
    :type line_length: int
    :param word_length: The length of the word. Default is 10
    :type word_length: int
    :returns: string - The generated line of words
    """
    line = ' '.join([gen_random_string(word_length) for i in range(line_length)])
    return line

def gen_lines(num = 200, line_len = 10, word_length = 10):
    """Generates the specified number of lines with the specified number of 
    words that consist of random letters.

    :param num: Number of lines to generate. Default is 200
    :type num: int
    :param line_len: The length of a line in words. Default is 10
    :type line_len: int
    :param word_length: The length of the word. Default is 10
    :type word_length: int
    :returns: string - The generated lines
    """
    lines = '\n'.join([gen_line(line_len, word_length) for i in range(num)])
    return lines

def main():
    """The main entry point for the script
    """
    try: 
        num_lines = int(input(Fore.GREEN + "How many lines of text would you like to have? Please, enter a number: " + Fore.YELLOW))
        line_length = int(input(Fore.GREEN + "How many words would you like to have in a line? Please, enter a number: " + Fore.YELLOW))
        word_length = int(input(Fore.GREEN + "How long would you like each word to be? Please, enter a number: " + Fore.YELLOW))
    except ValueError as ve:
        print(Back.RED + Fore.WHITE + f"Oops! This doesn't appear to be a number...\n{ve}")
        exit(1)

    # Ask for the file directory input
    dir_path = input(Fore.GREEN + "Please specify the directory where the text file should be saved: " + Fore.YELLOW)
    file_path = os.path.join(dir_path, 'random.txt')

    # Generate the lines
    lines = gen_lines(num_lines, line_length, word_length)

    # Write the text into a file
    try:
        with open(file_path, 'w') as f:
            f.write(lines)
            f.close()
    except OSError as ose:
        print(Back.RED + Fore.WHITE + f"Oops! This doesn't appear to be a valid directory path...\n{ose}")
        exit(1)

    print(Fore.GREEN + f"\n\nYou can find {num_lines} lines of text in file '" + Fore.YELLOW + f"{file_path}'")

if __name__ == "__main__":
    # Initializes colorama
    init()
    # The main program starts here
    main()
