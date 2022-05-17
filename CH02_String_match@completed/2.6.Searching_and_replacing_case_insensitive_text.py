#search in a case insensitive way

import re
text = "UPPER PYTHON, Mixed PyThon, lower python"
print(re.findall("python", text, flags=re.IGNORECASE))

print(re.sub("python", 'Go', text, flags=re.IGNORECASE))

def matchcase(word):
    def replace(m):
        g = m.group()
        if g.isupper():
            return word.upper()
        elif g.islower():
            return word.lower()
        elif g[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase("snake"), text, flags=re.IGNORECASE))

