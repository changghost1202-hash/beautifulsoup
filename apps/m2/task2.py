from bs4 import SoupStrainer
from bs4 import BeautifulSoup
import sys
import os

if len(sys.argv) < 2:
    print("Please input the test file path")
    sys.exit()
if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit()

only_a_tag = SoupStrainer("a")

# Read HTML content from a file
with open(sys.argv[1], 'r') as file:
    html_cont = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser', parse_only = only_a_tag).prettify()

print(soup)



