import unittest
#from htmlnode import markdown_to_html_node, to_html
from markdown_to_html import markdown_to_html_node, extract_title, generate_page


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
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


    def test_complex_quoteblock(self):
        md = """
> quote blocks are a bit different,
>they may or may not have a 
> space after the first character, so should be _treated_ **as
>one** block of text. 
> There might also be an
>
>empty line in this
> scenario"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = """<div><blockquote>quote blocks are a bit different, they may or may not have a space after the first character, so should be <i>treated</i> <b>as one</b> block of text. There might also be an empty line in this scenario</blockquote></div>"""
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

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
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

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
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


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
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

    def test_paragraph_link(self):
        md = """This is a link to [Markdown](https://www.markdownlang.com)"""
        expected = """<div><p>This is a link to <a href="https://www.markdownlang.com">Markdown</a></p></div>"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


    def test_paragraph_pics(self):
        md = """test paragraph pics ![image](https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png) hope it works!
"""


        expected = """<div><p>test paragraph pics <img src="https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png" alt="image"></img> hope it works!</p></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

    def test_code_paragraph_pics(self):
        md = """```
test paragraph pics ![image](https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png) hope it works!```
"""


        expected = """<div><pre><code>test paragraph pics ![image](https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png) hope it works!</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

    def test_ul_link(self):
        md = """
- unordered link line 1
- unordered link line 2
- unordered link line 3
"""


        expected = """<div><ul><li>unordered link line 1</li><li>unordered link line 2</li><li>unordered link line 3</li></ul></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

    def test_code_ul_link(self):
        md = """```
- unordered link line 1
- unordered link line 2
- unordered link line 3```"""


        expected = """<div><pre><code>- unordered link line 1
- unordered link line 2
- unordered link line 3</code></pre></div>"""


        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


    def test_code_ol_formatting(self):
        md = """```
1. ordered list one **with** bold formatting
2. ordered list two _with_ italic formatting
3. ordered list three `with` code formatting
4. ordered list four with random #hastags#
```"""

        expected = """<div><pre><code>1. ordered list one **with** bold formatting
2. ordered list two _with_ italic formatting
3. ordered list three `with` code formatting
4. ordered list four with random #hastags#
</code></pre></div>"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


    def test_ol_formatting(self):
        md = """
1. ordered list one **with** bold formatting
2. ordered list two _with_ italic formatting
3. ordered list three `with` code formatting
4. ordered list four with random #hastags#
"""

        expected = """<div><ol><li>ordered list one <b>with</b> bold formatting</li><li>ordered list two <i>with</i> italic formatting</li><li>ordered list three <code>with</code> code formatting</li><li>ordered list four with random #hastags#</li></ol></div>"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")

    def test_ol_double_digit_formatting(self):
        md = """
1. ordered list one **with** bold formatting
2. ordered list two _with_ italic formatting
3. ordered list three `with` code formatting
4. ordered list four with random #hastags#
5. five
6. six
7. seven
8. eight
9. nine
10. ten
11. eleven
12. twelve
"""

        expected = """<div><ol><li>ordered list one <b>with</b> bold formatting</li><li>ordered list two <i>with</i> italic formatting</li><li>ordered list three <code>with</code> code formatting</li><li>ordered list four with random #hastags#</li><li>five</li><li>six</li><li>seven</li><li>eight</li><li>nine</li><li>ten</li><li>eleven</li><li>twelve</li></ol></div>"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


    def test_ol_pics_links(self):
        md = """
1. ordered list one **with** pic ![image](https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png) inline 
2. ordered list two _with_ link [Markdown](https://www.markdownlang.com) inline
"""

        expected = """<div><ol><li>ordered list one <b>with</b> pic <img src="https://www.kasandbox.org/programming-images/avatars/duskpin-tree.png" alt="image"></img> inline</li><li>ordered list two <i>with</i> link <a href="https://www.markdownlang.com">Markdown</a> inline</li></ol></div>"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")




    def test_quote_basic_markdown_to_html(self):
        md = """> quote first line
> quote second line of text
>quote third line of text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = """<div><blockquote>quote first line quote second line of text quote third line of text</blockquote></div>"""
        self.assertEqual(html, expected, f"\n  actual: {html!r}\nexpected: {expected!r}")


class test_extract_title(unittest.TestCase):
    def test_one_line_one_header(self):
        print(f"testing extract title")    
        markdown = "# SIMPLE TEST CASE"
        title = extract_title(markdown)
        expected = "SIMPLE TEST CASE"
        self.assertEqual(title, expected)


class test_generate_page(unittest.TestCase):
    def test_easy_page(self):
        print(f"testing generate page")
        full_html_file = generate_page("content/index.md", "template.html", "public")

    def test_easy_page_w_new_folder(self):
        print(f"testing generate page")
        full_html_file = generate_page("content/index.md", "template.html", "skibbidy")
