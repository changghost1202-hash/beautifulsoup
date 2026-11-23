"""Milestone 4: lazy iteration over nodes in a BeautifulSoup document."""

import pytest

from bs4 import BeautifulSoup
from bs4.element import Comment, Doctype, NavigableString, Tag


def test_nested_tags_use_depth_first_document_order():
    soup = BeautifulSoup('<div><p>Hello <b>world</b></p><br/></div>', 'html.parser')
    nodes = iter(soup)
    assert next(nodes) is soup.div
    assert next(nodes) is soup.p
    assert next(nodes) is soup.p.contents[0]
    assert next(nodes) is soup.b
    assert next(nodes) is soup.b.string
    assert next(nodes) is soup.br
    with pytest.raises(StopIteration):
        next(nodes)


def test_text_only_document():
    soup = BeautifulSoup('Just plain text', 'html.parser')
    nodes = iter(soup)
    text = next(nodes)
    assert isinstance(text, NavigableString)
    assert str(text) == 'Just plain text'
    with pytest.raises(StopIteration):
        next(nodes)


def test_comment_and_doctype_nodes():
    soup = BeautifulSoup('<!DOCTYPE html><!--note--><p>hello</p>', 'html.parser')
    nodes = iter(soup)
    assert isinstance(next(nodes), Doctype)
    comment = next(nodes)
    assert isinstance(comment, Comment)
    assert str(comment) == 'note'
    assert next(nodes) is soup.p
    assert next(nodes) is soup.p.string
    with pytest.raises(StopIteration):
        next(nodes)


def test_empty_document():
    soup = BeautifulSoup('', 'html.parser')
    nodes = iter(soup)
    assert iter(nodes) is nodes
    with pytest.raises(StopIteration):
        next(nodes)


def test_independent_lazy_iterators_and_regular_tag_behavior():
    soup = BeautifulSoup('<div><span>first</span></div>', 'html.parser')
    first = iter(soup)
    second = iter(soup)
    assert first is not second
    assert next(first) is soup.div
    assert next(second) is soup.div
    assert next(first) is soup.span

    # Verify the iteration is not a precomputed snapshot of all nodes.
    new_tag = soup.new_tag('em')
    new_tag.string = 'later'
    soup.div.append(new_tag)
    assert next(first) is soup.span.string
    assert next(first) is new_tag
    assert next(first) is new_tag.string
    with pytest.raises(StopIteration):
        next(first)

    # A normal Tag still iterates over direct children only.
    assert next(iter(soup.div)) is soup.span
    assert isinstance(soup.div, Tag)