from collections import defaultdict

def default_dict_test():
    dd = defaultdict(list)
    #feed in a class object
    # dd = defaultdict(set)
    # dd["xx"].add()
    dd['a'].append(1)
    dd['a'].append(2)
    dd['b'].append(4)
    print(dd)
    print("c" in dd)

def ordinary_dict_test():
    d = {}
    d.setdefault("a", []).append(1)
    d.setdefault("a", []).append(2)
    d.setdefault("b", []).append(4)
    print(d)
    print("c" in d)



if __name__ == "__main__":
    ordinary_dict_test()
    default_dict_test()