from collections import OrderedDict
import json
# note: Hash Doubly linked list built internally
# twice memory as much as common dict

d = OrderedDict()
d["ryu"] = 1
d["ken"] = 2
d["luke"] = 3
d["sakura"] = 4
print(d)

"""
dumps() method allows us to convert a python object into an equivalent JSON object. 
Or in other words to send the data from python to json. The json. dump() method allows 
us to convert a python object into an equivalent JSON object and store the result into 
a JSON file at the working directory.
"""
j = json.dump(d)
print(j)