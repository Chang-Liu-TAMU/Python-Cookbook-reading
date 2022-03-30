# @Time: 2022/3/29 11:14
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:2.12.Sanitizing_and_clearing_up_text.py

s = "pýtĥöñ\fis\tawesome\r\n"
print("\f")
print(s)

remap = {
    ord("\t"): " ",
    ord("\f"): " ",
    ord("\r"): None # deleted carriage return
}

a = s.translate(remap)
print(a)

print("*" * 30)
import unicodedata
import sys
cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode)
                          if unicodedata.combining(chr(c)))
b: str = unicodedata.normalize("NFD", a)
print("NFD: ", b)
print(b.translate(cmb_chars))

print("*" * 30)
# x = unicodedata.digit("1")
# print(x, type(x))
# print("chr(0) = ", chr(0))
digitmap = {c: ord("0") + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == "Nd"}

print(len(digitmap))
x = "\u0661\u0662\u0663"
print(x)
print(x.translate(digitmap))
# print("\u3041")

print("$" * 30)
print(a)
b = unicodedata.normalize("NFD", a)
print(b.encode("ascii", "ignore").decode("ascii"))


print("*" * 30)

def clean_spaces(s):
    #a little bit faster
    s = s.replace("\r", "")
    s = s.replace("\t", "")
    s = s.replace("\f", "")
    return s

print(clean_spaces(s))

