import re

name = "a is called \"ryu\""
p_greedy = re.compile(r"\"(.*)\"") #() gives grouping, only find groups
print(p_greedy.findall(name))

#' differs from "
name = 'a is called "ryu", b is called "sakura"'
print(p_greedy.findall(name))

#without ?, just greedy matching (longest)

p_non_greedy = re.compile(r"\"(.*?)\"")
print(p_non_greedy.findall(name))
