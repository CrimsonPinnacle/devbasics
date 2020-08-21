#!/usr/bin/python

import logging
import os
import string
import sys

from random import choices
from colorama import init, Fore, Back

"""
.. module:: random_text_v4
:platform: Unix, Windows
:synopsis: Example script demonstrating the use of log levels in Python

.. moduleauthor:: Toddy Mladenov <toddysm@gmail.com>
"""

# Configure logging
log_msg_format = "%(asctime)s (%(module)s --> %(funcName)s[%(lineno)d]) [%(levelname)s]: %(message)s"
log_level = logging.DEBUG
logging.basicConfig(filename=f"randomtext_l{log_level}.log", filemode='w', format=log_msg_format, level=log_level)

def gen_random_string(length = 10):
    """Generates a random string with the specified lenght. The string is made
    of letters only.

    :param length: The length of the string to generate. Default is 10
    :type length: int
    :returns: string - The random string
    """
    logging.debug(f"Generating word with length {length}")
    word = ''.join(choices(string.ascii_letters, k=length))
    logging.debug(f"Generated word {word}")
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
    logging.debug(f"Generating line with length {line_length} and word length {word_length}")
    line = ' '.join([gen_random_string(word_length) for i in range(line_length)])
    logging.debug(f"Generated line with length {len(line)}")
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
    logging.debug(f"Generating {num} number of lines with {line_len} line length and {word_length} word length")
    lines = '\n'.join([gen_line(line_len, word_length) for i in range(num)])
    logging.debug(f"Generated random text with length {len(lines)}")
    return lines

def main():
    """The main entry point for the script
    """
    logging.debug("Prompting user for input...")
    while(True):
        try: 
            num_lines = int(input(Back.BLACK + Fore.GREEN + "How many lines of text would you like to have? Please, enter a number: " + Fore.YELLOW + Back.BLACK ))
            line_length = int(input(Fore.GREEN + "How many words would you like to have in a line? Please, enter a number: " + Fore.YELLOW))
            word_length = int(input(Fore.GREEN + "How long would you like each word to be? Please, enter a number: " + Fore.YELLOW))
            break
        except ValueError as ve:
            #logging.exception("Invalid user input.")
            print(Back.RED + Fore.WHITE + f"Oops! This doesn't appear to be a number...\nPlease try again!")
            logging.warning(f"Non number provided by the user: {ve}")

    logging.debug(f"User input completed! Number of lines: {num_lines}; Line length: {line_length}; Word length: {word_length}")

    # Ask for the file directory input
    logging.debug("Prompting user for directory path...")
    dir_path = input(Fore.GREEN + "Please specify the directory where the text file should be saved: " + Fore.YELLOW)
    file_path = os.path.join(dir_path, 'random.txt')
    logging.debug(f"File path {file_path}")

    # Generate the lines
    lines = gen_lines(num_lines, line_length, word_length)

    # Write the text into a file
    try:
        logging.debug("Writing random text to file...")
        with open(file_path, 'w') as f:
            f.write(lines)
            f.close()
        logging.debug("Writing random text to file completed!")
    except OSError as ose:
        logging.exception("Invalid directory path.")
        print(Back.RED + Fore.WHITE + f"Oops! This doesn't appear to be a valid directory path...\n{ose}")
        logging.critical("Wrong directory path provided by the user")
        exit(1)

    print(Fore.GREEN + f"\n\nYou can find {num_lines} lines of text in file '" + Fore.YELLOW + f"{file_path}'")

if __name__ == "__main__":
    logging.info(f"Starting random text generation session...")
    # Initializes colorama
    init()
    # The main program starts here
    main()
    logging.info("Random text generation completed!")