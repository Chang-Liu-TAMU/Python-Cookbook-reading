x = "\u00f1"
s1 = f"Spicy Jalape{x}o"
print(x)
s2 = "Spicy Jalapen\u0303o"
print("\u0303")

print("s1: ", s1, "len(s1): ", len(s1))
print("s2: ", s2, "len(s2): ", len(s2))
print(s1 == s2)

print("*" * 30)

import unicodedata
t1 = unicodedata.normalize("NFC", s1) # "C": composed, maybe compressed, less is better
t2 = unicodedata.normalize("NFC", s2) # "NFD": "D" means decomposed, more is better

print(t1, t2)
print(ascii(t1), ascii(t2))
print(len(t1), len(t2))

print("*" * 30)
s = "\ufb01"
print(s, len(s))
s_nfd = unicodedata.normalize('NFD', s)
print(s_nfd, len(s_nfd))
#even using "NFD", we can not decouple it

s_nfkd = unicodedata.normalize("NFKD", s)
print(s_nfkd, len(s_nfkd))

s_nfkc = unicodedata.normalize("NFKC", s)
print(s_nfkc, len(s_nfkc))

print("*" * 30)
print("s1: ", s1)
print("filtering s1...")
t1 = unicodedata.normalize("NFD", s1)
print("after filtering combining characters:")
print("".join(c for c in t1 if not unicodedata.combining(c)))
