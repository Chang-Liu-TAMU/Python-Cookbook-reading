# @Time: 2022/3/31 9:18
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.17.Handling_HTML_and_XML_Entities_in_Text.py


s = 'Elements are written as "<tag>text</tag>"'
import html
print(s)
print(html.escape(s))


print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
# print(ord("ñ"))
print(s.encode("ascii", errors="xmlcharrefreplace"))


s = 'Spicy &quot;Jalape&#241;o&quot.'
import html
print(html.unescape(s))


t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))