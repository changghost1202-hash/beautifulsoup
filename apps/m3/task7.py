from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
import sys
import os


def change_attrs(tag):
    attrs = dict(tag.attrs)

    if tag.name == 'p':
        attrs['class'] = ['test']

    return attrs


if len(sys.argv) < 2:
    print("Please input the test file path")
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit()

# Read HTML content from a file
with open(sys.argv[1], 'r') as file:
    html_cont = file.read()

# Create SoupReplacer
replacer = SoupReplacer(attrs_xformer=change_attrs)

# Parse HTML and transform tags during parsing
soup = BeautifulSoup(
    html_cont,
    'html.parser',
    replacer=replacer
)

# Write the modified tree to a file
with open('output7.html', 'w') as file:
    file.write(soup.prettify())