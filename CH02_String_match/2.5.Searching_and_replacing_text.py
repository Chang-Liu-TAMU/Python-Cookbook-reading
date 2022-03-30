text = "a a a b b a a"
print(text.replace("a", "b"))
#replace "a" with "b"

text = "today is 3/18/2022, tomorrow is 3/19/2022"
import re
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3--\1--\2", text))

#first compile a re pattern to improve performance
p = re.compile(r"(\d+)/(\d+)/(\d+)")
print(p.sub(r"\3--\1--\2", text))

from calendar import month_abbr
# print(month_abbr)
# define a callback function replacing r"\3--\1--\2"
a = 0
def callback(m):
    """
    :param m: a re match object
    :return:
    """
    print(a)
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"
print(p.sub(callback, text))

newtext, n = p.subn(r"\3--\1--\2", text)
print(newtext, n)