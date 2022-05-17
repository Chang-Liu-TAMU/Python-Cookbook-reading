l = [{}] #list with elements
#sort(l, key=?)
#min(l, key=?)
#max(l, key=?)

#common way
key1 = lambda x: x["some_key"]

# a faster way
from operator import itemgetter
#if a object support __getitem__, use itemgetter
key2 = itemgetter("key1", 'key2', "etc")

if __name__ == "__main__":
    # a = [1, 2]
    class MyList(list):
        def __getitem__(self, item):
            return super().__getitem__(item+1)
    a = MyList([1, 2])
    print(a[0])