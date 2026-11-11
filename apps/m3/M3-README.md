# Milestone-3
## 1. Overview

In Milestone 3, I extended the `SoupReplacer` API from Milestone 2 to support more flexible HTML tag transformations during parsing.

The original API only allowed users to replace one specific tag name with another. The new API allows users to provide custom functions to modify tag names, attributes, or tag objects directly.

## 2. Milestone 2 API

In Milestone 2, `SoupReplacer` supported a simple replacement interface:

```python
SoupReplacer("b", "blockquote")
```

This API is easy to understand and use. However, it only supports fixed tag-name replacements and cannot make decisions based on a tag's attributes or other properties.

## 3. Milestone 3 API

In Milestone 3, I added three optional function arguments:

```python
SoupReplacer(
    name_xformer=None,
    attrs_xformer=None,
    xformer=None
)
```

Each function serves a different purpose:

- `name_xformer`: Returns a new name for the tag.
- `attrs_xformer`: Returns a new dictionary of tag attributes.
- `xformer`: Directly modifies the tag object without returning a value.

For example:

```python
def change_name(tag):
    if tag.name == "b":
        return "blockquote"
    return tag.name

replacer = SoupReplacer(name_xformer=change_name)
```

This approach allows users to define their own transformation rules without modifying the BeautifulSoup source code.

## 4. Implementation Challenges

One challenge was handling opening and closing tags correctly when a tag name was changed during parsing.

For example, when `name_xformer` changes `<b>` into `<blockquote>`, the parser still receives the original closing tag `</b>`. If the parser uses the transformed name for matching, it may fail to close the correct tag.

To solve this issue, I stored the original tag names separately and used them for parsing operations, while keeping the transformed names in the resulting HTML tree.

I also updated the tag stack management and tag counter logic to ensure that nested tags could still be handled correctly.

## 5. Comparison and Recommendation

The Milestone 2 API is simpler and more suitable for basic tag replacements. The Milestone 3 API is more flexible because users can define conditional transformations and modify multiple properties of a tag.

However, the new API is also more complex, and user-defined functions may introduce unexpected side effects.

**I recommend keeping both APIs** to maintain backward compatibility while supporting more advanced transformations.

The implementation should clearly document the purpose and execution order of each transformer. It should also preserve the original tag information needed by the parser to maintain a correct HTML tree.

This approach provides a good balance between simplicity, flexibility, and maintainability.

## 6. Testing

I added six new test cases to verify the Milestone 3 API, covering:

1. Tag name transformation
2. Attribute transformation
3. Direct tag modification
4. Combined transformations
5. No transformers provided
6. Nested tag transformations

All six new tests passed, along with the two existing Milestone 2 tests.

I also implemented Milestone 1 Task 7 using `attrs_xformer` to add or replace the `class` attribute of all `<p>` tags with `class="test"` during parsing.

The modified HTML tree is written to an output file.

## 7. Conclusion

The Milestone 3 API makes `SoupReplacer` more extensible by allowing users to provide custom transformation functions.

Although it introduces additional implementation complexity, it provides greater control over HTML transformations without requiring changes to the library's core code for each new use case.

For a potential BeautifulSoup extension, I would recommend maintaining the simple replacement interface from Milestone 2 while offering the transformer-based interface as an advanced option.
