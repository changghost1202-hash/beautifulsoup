from bs4 import BeautifulSoup
from bs4 import SoupStrainer
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

True_id_tag = SoupStrainer(id = True)
# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser', parse_only=True_id_tag)

print(soup)
