#Task 2: Word Frequency Create a program that reads a created text file from task 1 and counts the frequency of each word.   

import requests
from bs4 import BeautifulSoup
from collections import Counter
import string

def scrape_python_org():
    url = "https://www.python.org/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = ""
        for element in soup.find_all(["p", "h1", "h2", "h3"]):
            text += element.get_text() + "\n"
        with open("python_org_text.txt", "w",) as file:
            file.write(text)

        print("Task 1: Data has been scraped and saved to python_org_text.txt.")
    else:
        print("Task 1: Failed to retrieve data from Python.org.")
# Read the text file and converting to lower case 
def count_word_frequency(filename):
    with open(filename, "r") as file:
        text = file.read().lower()  
#  Remove the punctuation and split the text into words 
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()
# count the frequency of each word using counter 
    word_frequency = Counter(words)
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    scrape_python_org()
    count_word_frequency("python_org_text.txt")
