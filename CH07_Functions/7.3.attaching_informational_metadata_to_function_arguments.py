# @Time: 2022/5/7 18:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:7.3.attaching_informational_metadata_to_function_arguments.py

def add(x: int, y: int) -> int:
    return x + y

# print(help(add))

#function is also a object
print(add.__annotations__)