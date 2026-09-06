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


    def test_simple_quoteblock(self):
        md = """
> quote blocks are a bit different,
>they may or may not have a 
> space after the first character, so should be _treated_ **as
>one** block of text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = """<div><blockquote>quote blocks are a bit different, they may or may not have a space after the first character, so should be <i>treated</i> <b>as one</b> block of text</blockquote></div>"""
        self.assertEqual(html, expected)

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

```
and of course the 
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
        html = node.to_html()
        expected = """<div><p>unformatted paragraph</p><p>formatted <b>bold</b> <i>italic</i> paragraph</p><h1>Header 1</h1><h2>header 2</h2><ul><li>unordered <b>list</b> item 1</li><li>unordered <i>list</i> item 2</li><li>unordered list item 3</li></ul><ol><li>numbered list one</li><li>numbered list two</li><li>numbered list three</li></ol><pre><code>and of course the 
infamous clode block
which will not be **bold** formatted</code></pre><blockquote>quote blocks are a bit different, they may or may not have a space after the first character, so should be <i>treated</i> <b>as one</b> block of text</blockquote><h3>other things to check:</h3><ul><li>formatting inside each block</li><li>image links</li><li>html links</li><li>malformed markdown</li><li>bold in headers</li><li>more than 6 # headers</li><li>two header lines together</li></ul><h5>5 header</h5><h6>6 header</h6><p>####### 7 header</p></div>"""
        self.assertEqual(html, expected)

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

        expected = """<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)


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


        expected = """<div><pre><code># here's some comments
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
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def test_paragraph_link(self):
        md = """This is a link to [Markdown](https://www.markdownlang.com)
"""


        expected = """<div><p>This is a link to <a href="https://www.markdownlang.com">Markdown</a></p></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def test_paragraph_pics(self):
        md = """test paragraph pics ![image](https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png) hope it works!
"""


        expected = """<div><p>test paragraph pics <img src="https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png" alt="image"></img> hope it works!</p></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_ul_link(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_ul_pics(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_ol_link(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_ol_pics(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_paragraphs_newlines(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)

    def dont_test_everything(self):
        md = """```
```"""


        expected = """<div><pre><code># here's some comments
5. some non md files\n</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\n\n[actual]\n\n{html}\n\n[expected]\n\n{expected}\n\n")
        self.assertEqual(html, expected)


    def test_quote_basic_markdown_to_html(self):
        md = """> quote first line
> quote second line of text
>quote third line of text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = """<div><blockquote>quote first line quote second line of text quote third line of text</quoteblock></div>"""
        #print(f"[md]\n{md}\n\n[node]\n{node}\n\n[html]\n{html}\n\n[expected]\n{expected}\n\n")
        #self.assertEqual(html, expected)

    def dont_test_block_splitter_quote_missing(self):
        block = """> quote first line
quote second line of text
>quote third line of text"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARA)

    def dont_test_block_splitter_quote_double(self):
        block = """>> quote first line
>>> quote second line of text
>>>>quote third line of text"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOT)

    def dont_test_block_splitter_quote_midline(self):
        block = """quote > mid line
>>> quote second line of text
>>>>quote third line of text"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARA)





#other ideas
# paragraphs with other line breaks
# paragraphs into unordered and numbered lists, code, 
# paragraphs with pics
# paragraphs with links
# uo lists with pics
# uo lists with links
# ol lists with pics
# ol lists with links
