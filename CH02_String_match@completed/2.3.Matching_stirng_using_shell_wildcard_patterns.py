#wildcard

from fnmatch import fnmatch, fnmatchcase
print(fnmatch("foo.txt", "*.txt"))

print(fnmatch("foo.txt", "?oo.txt"))

print(fnmatch("Dat45.csv", "Dat[0-9]*v"))

names = ["abc.py", "Dat01.csv", "Dat99.csv", 'cde.ini']
print([name for name in names if fnmatch(name, "*.csv")])

print(fnmatch("foo.txt", "*.TxT"))
# if os X
# fnmatch("foo.txt", "*.TXT") -> False

print(fnmatch("foo.txt", "*.TXT"))

addresses = [
    "324 A ADFI ST",
    "234 D efae ST",
    "afew d DF AVE",
    "909 F jfoe ST"
]

print([name for name in addresses if fnmatchcase(name, "*ST")])
print([name for name in addresses if fnmatchcase(name, "[0-9][0-9]4*")])