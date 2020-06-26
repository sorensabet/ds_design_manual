from lxml import html
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Step 1. Scrape the best-seller rank for a book on Amazon.com. Scope down to Hardcovers
# Step 2. Get ranks for all of Skiena's books.
# Step 3. Which one should be the next item purchased?

# Given that there are a small number of books, best to just get the direct link of each page and then

alg_des_man = 'https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena-dp-1848000693/dp/1848000693/ref=mt_hardcover?_encoding=UTF8&me=&qid=1587875161'
ds_des_man = 'https://www.amazon.com/Science-Design-Manual-Texts-Computer-dp-3319554433/dp/3319554433/ref=mt_hardcover?_encoding=UTF8&me=&qid=1587875161'
calc_bets = 'https://www.amazon.com/Calculated-Bets-Computers-Gambling-Mathematical-dp-0521804264/dp/0521804264/ref=mt_hardcover?_encoding=UTF8&me=&qid=1587875161'
prog_chal = 'https://www.amazon.com/Programming-Challenges-Contest-Training-Computer/dp/0387001638/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1587875161&sr=1-4'

urls = [alg_des_man, ds_des_man, calc_bets, prog_chal]

# For each book:
# Get html of web page
# Get relevant div
# Scrape out best selers rank for books

#productDetailsTable
for url in urls:
    html = requests.get(url).text
    # Turns out that Amazon blocks web scraping, this excercise is no longer useful for learning D.S.
    # I looked at html of page and found the id of the productDetails table, I would extract that, use a regex to get bestseller rank, and compare between the books.
    # To do it over time, automate this code to run for a while.

    print('')