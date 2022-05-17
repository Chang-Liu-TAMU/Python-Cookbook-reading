if False:
    a = "xx.txt"
    print(a.endswith(".txt"))
    b = "http://0.0.0.0"
    print(b.startswith("http"))

if False:
    import os
    filenames = os.listdir(".")
    print([file for file in filenames if file.endswith(".py")])
    print(any(file.endswith(".cpp") for file in filenames))

if False:
    from urllib.request import urlopen

    def read_data(name):
        #s.startswith(a tuple), list is not acceptable
        if name.startswith(("http:", "https:", "ftp:")):
            return urlopen(name).read()
        else:
            with open(name) as f:
                return f.read()

    choices = ["http:", "ftp:"]
    url = "http://www.python.org"
    try:
        url.startswith(choices)
    except Exception as e:
        print(e)
    finally:
        choices = tuple(choices)
        print(url.startswith(choices))


if True:
    name = "abc.txt"
    print(name[-4:] == ".txt")
    #not elegant
    import re
    url = "http://www.python.org"
    print(re.match("http:|https|ftp", url))

    if any(name.endswith((".h", ".c")) for name in os.listdir("./somepath")):
        #check presence of files of certain type
        pass