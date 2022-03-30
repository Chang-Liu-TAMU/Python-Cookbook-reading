import re
c_style_string = """*/ time leaves no trace
                it can not change my heart */
"""

# dot . matches any except newline

p = re.compile(r"\*/(.*?)\*/")
print(p.findall(c_style_string))

p = re.compile(r"\*/(.*?)\*/", flags=re.DOTALL)
print(p.findall(c_style_string))

p = re.compile(r"\*/((?:.|\n)*?)\*/")
# ?: means no grouping , only matching
print(p.findall(c_style_string))

