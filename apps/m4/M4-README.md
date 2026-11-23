# Milestone 4 — Iterable BeautifulSoup

## Overview

This milestone makes a `BeautifulSoup` object iterable. After parsing an HTML document, users can write `for node in soup` to visit all descendant nodes in depth-first document order. The original `BeautifulSoup(html_doc, 'html.parser')` constructor remains unchanged.

The iterator visits `Tag`, `NavigableString`, `Comment`, and `Doctype` nodes. It does not yield the synthetic `[document]` root itself.

## Implementation

**File:** `bs4/__init__.py`, inside `class BeautifulSoup(Tag)`.

```python
def __iter__(self) -> Iterator[PageElement]:
    return self.descendants
```

`self.descendants` is an existing generator from `bs4/element.py`. It starts at the first child and follows each node's `next_element` link until it passes the last descendant of the current tree. Its `yield current` statement produces one node at a time and suspends execution until the next item is requested.

The implementation **does not collect all nodes into a list**. Walking N nodes takes O(N) time and O(1) additional traversal space (excluding the already parsed HTML tree). Each call to `iter(soup)` creates an independent iterator. Regular `Tag` objects still iterate over their direct children only.

## Usage

```python
from bs4 import BeautifulSoup
from bs4.element import Tag

html_doc = '<div><p>Hello <b>World</b></p></div>'
soup = BeautifulSoup(html_doc, 'html.parser')

for node in soup:
    if isinstance(node, Tag):
        print('Tag:', node.name)
    else:
        print('Text:', repr(str(node)))
```

Expected output:

```text
Tag: div
Tag: p
Text: 'Hello '
Tag: b
Text: 'World'
```

Calling `print(node)` directly is also supported, but it prints the entire nested markup for a `Tag`, so parts of the HTML will appear more than once.

## Unit Tests

**File:** `bs4/tests/test_iteration.py`

Five tests cover:

1. Nested tags, text, and empty tags in depth-first order.
2. A text-only document.
3. Doctype and comment nodes.
4. Empty documents and proper `StopIteration` at the end.
5. Independent iterators, lazy traversal after a tree modification, and unchanged iteration behavior for regular tags.

Run the tests from the repository root:

```bash
python -m pytest bs4/tests/test_iteration.py -v
```

