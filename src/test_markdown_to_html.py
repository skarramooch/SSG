import unittest
#from htmlnode import markdown_to_html_node, to_html
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_simplemarkdown(self):
        md = """simple **I said SIMPLE** text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>simple <b>I said SIMPLE</b> text</p></div>",
        )


    def test_simple_block(self):
        md = """unformatted paragraph

formatted **bold** _italic_ paragraph

# Header 1

## header 2

- unordered **list** item 1
- unordered _list_ item 2
- unordered list item 3

1. numbered list one
2. numbered list two
3. numbered list three

```and of course the 
infamous clode block
which will not be **bold** formatted```

> quote blocks are a bit different,
>they may or may not have a 
> space after the first character, so should be _treated_ **as
>one** block of text

### other things to check:
- formatting inside each block
- image links
- html links
- malformed markdown
- bold in headers
- more than 6 # headers
- two header lines together

##### 5 header

###### 6 header

####### 7 header"""
        node = markdown_to_html_node(md)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_tabbed_numbered_codeblock(self):
        md = """```
# here's some comments
##here's a couple more, I hope they
###dont get trated as headers!!
def dprint(*kargs, **kwargs):
    if DPRINT:
        print(*kargs, **kwargs)
#drpint statement finished
<h1>other ideas for testing</h1>
1. numbered blocks (done)
2. images
3. links
4. not separated paragraphs
5. some non md files
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><pre><code># here's some comments
##here's a couple more, I hope they
###dont get trated as headers!!
def dprint(*kargs, **kwargs):
    if DPRINT:
        print(*kargs, **kwargs)
#drpint statement finished
<h1>other ideas for testing</h1>
1. numbered blocks (done)
2. images
3. links
4. not separated paragraphs
5. some non md files\n</code></pre></div>""",
        )


#other ideas
# paragraphs with other line breaks
# paragraphs into unordered and numbered lists, code, 
# paragraphs with pics
# paragraphs with links
# uo lists with pics
# uo lists with links
# ol lists with pics
# ol lists with links
