from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div>
            <p>Hello <b>World</b></p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

for node in soup:
    print(node)