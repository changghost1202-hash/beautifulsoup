# Milestone-2
## Part 2
### Milestone 1 APIs

| API | Source File | Line Number |
|---|---|---|
| BeautifulSoup constructor | bs4/__init__.py | 209 |
| find_all() | bs4/element.py | 2715 |
| prettify() | bs4/element.py | 2601 |
| find_parent() | bs4/element.py | 992 |
| find_next_sibling() | bs4/element.py | 803 |

### Milestone 2 Part 1 APIs

| API | Source File | Line Number |
|---|---|---|
| SoupStrainer constructor | bs4/filter.py | 345 |
| parse_only parameter | bs4/__init__.py | 214 |
| prettify() | bs4/element.py | 2601 |

## Part 3 How to Use SoupReplacer
1. Import BeautifulSoup and SoupReplacer.
```python
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
```
2. Initialize a SoupReplacer object : the first string is the tag name you want to find and replace. The second string is the new tag name you want to use as a replacement.
```python
replacer = SoupReplacer("b", "blockquote")
```
3. Initialize a BeautifulSoup object : Pass the replacer created in the previous step to the BeautifulSoup constructor.
```
soup = BeautifulSoup(html_cont, 'html.parser', replacer=replacer)
```
4. Print the parsed HTML and compare it with the original HTML.
```python
print(soup.prettify())
```

## How to use task6.py
1. Check the test html file path.
2. Open the terminal and navigate to the beautifulsoup/apps/m2 directory.
3. type the following command.
```
python task6.py path/to/your/html/file.html
```
Note: Replace path/to/your/html/file.html with the actual path to your HTML file. Both absolute and relative paths are supported.

Note: This project includes a modified version of BeautifulSoup in the local bs4/ directory. To ensure that Python uses this version instead of an installed version, run the tasks from the project root directory with PYTHONPATH=.. For example:
```
PYTHONPATH=../.. python task6.py path/to/your/html/file.html
```
The output file, output6.html, will be saved in the current working directory.
