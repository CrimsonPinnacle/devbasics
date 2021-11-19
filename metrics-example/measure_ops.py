#!/usr/bin/python

import logging
import os
import requests
import string
import sys
import time
import validators

from bs4 import BeautifulSoup
from colorama import init, Fore, Back

"""
.. module:: measure_ops
:platform: Unix, Windows
:synopsis: Example script demonstrating how to collect performance metrics. The 
script downloads two web pages specified by the user and measures the time to
do the following operations:
- Download the page
- Find all headers on the page
- Prints the headers for each page on the screen
The implementation uses Python decorators to make the metrics collection easier.

.. moduleauthor:: Toddy Mladenov <toddysm@gmail.com>
"""

# Configure logging
log_msg_format = "%(asctime)s (%(module)s --> %(funcName)s[%(lineno)d]) [%(levelname)s]: %(message)s"
log_level = logging.DEBUG
logging.basicConfig(filename=f"randomtext_l{log_level}.log", filemode='w', format=log_msg_format, level=log_level)


def measure_ops(func):
    """Decorator function that measure the execution time of the provided function.

    :param func: The function to decorate
    :type func: function
    :returns: The function result
    """
    def inner(*args, **kwargs):
        start_time = time.time()
        return_val = func(*args, **kwargs)
        end_time = time.time()
        exec_time = round(end_time - start_time, 3)
        print(Fore.RED + f"Function `{func.__name__}` executed in {exec_time} seconds.")
        return return_val
    
    return inner

@measure_ops
def fetch_url(url):
    """Fetches the specified URL.

    :param url: The URL to fetch
    :type url: string
    :returns: The response object
    """
    return requests.get(url)

@measure_ops
def collect_all_links(soup):
    """Finds all links on the page and returns them as a list

    :param soup: The BeautifulSoup object
    :type soup: BeautifulSoup object
    :returns: List with URLs
    """
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    
    return links

@measure_ops
def collect_all_h1_headers(soup):
    """Finds all links on the page and returns them as a list

    :param soup: The BeautifulSoup object
    :type soup: BeautifulSoup object
    :returns: List with H1 headers text
    """
    h1_headers = []
    for header in soup.find_all('h1'):
        h1_headers.append(header.contents)
    
    return h1_headers

@measure_ops
def count_paragraphs(soup):
    """Counts the number of paragraphs ('p' tags) on the page

    :param soup: The BeautifulSoup object
    :type soup: BeautifulSoup object
    :returns: Integer with the number of paragraphs
    """
    paragraphs = len(soup.find_all('p'))
    return paragraphs

@measure_ops
def process_page(response):
    """Processes an HTML page. The things it does are:
    - Extracts all links
    - Extracts all H1 headers
    - Counts all paragraphs

    :param response: The HTTP response for the URL
    :type response: Response object
    :returns: None
    """
    soup = BeautifulSoup(response.content, 'html.parser')

    # collect all links first
    links = collect_all_links(soup)
    print(Fore.GREEN + f"There are " + Fore.YELLOW + str(len(links)) + Fore.GREEN + " links on this page:")
    # for link in links:
    #     print(Fore.YELLOW + str(link))

    # collect all H1 headers then
    headers = collect_all_h1_headers(soup)
    print(Fore.GREEN + f"There are " + Fore.YELLOW + str(len(headers)) + Fore.GREEN + " H1 headers on this page:")
    # for header in headers:
    #     print(Fore.YELLOW + str(header))

    # count the paragraphs at last
    print(Fore.GREEN + f"There are " + Fore.YELLOW + str(count_paragraphs(soup)) + Fore.GREEN + " paragraphs on this page:")

@measure_ops
def main():
    """The main entry point for the script
    """
    logging.debug("Prompting user for input...")
    while(True):
        try: 
            page1_url = input(Fore.GREEN + "Please, enter the URL for the first page: " + Fore.YELLOW)
            if not validators.url(page1_url):
                raise Exception()
            page2_url = input(Fore.GREEN + "Please, enter the URL for the second page: " + Fore.YELLOW)
            if not validators.url(page2_url):
                raise Exception()
            break
        except Exception as e:
            print(Back.RED + Fore.WHITE + f"Oops! This doesn't appear to be an URL...\nPlease try again!")
            logging.warning(f"Invalid URL string provided by the user: {e}")

    logging.debug(f"User input completed! First page URL is: {page1_url}\nSecond page URL is: {page2_url}")

    # process the 1st page
    response = fetch_url(page1_url)
    process_page(response)

    # process the 2nd page
    response = fetch_url(page2_url)
    process_page(response)

if __name__ == "__main__":
    logging.info(f"Starting performance sample session...")
    # Initializes colorama
    init()
    # The main program starts here
    main()
    logging.info("Performance sample session completed!")