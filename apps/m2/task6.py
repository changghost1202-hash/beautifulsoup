from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
import sys
import os

if len(sys.argv) < 2:
    print("Please input the test file path")
    sys.exit()
if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit()

# Read HTML content from a file
with open(sys.argv[1], 'r') as file:
    html_cont = file.read()

replacer = SoupReplacer("b", "blockquote")
# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser', replacer=replacer)

with open('output6.html', 'w') as file:
    file.write(soup.prettify())
