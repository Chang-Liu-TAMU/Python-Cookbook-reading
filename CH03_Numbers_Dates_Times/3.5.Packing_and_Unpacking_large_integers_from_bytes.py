# @Time: 2022/4/8 15:22
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:3.5.Packing_and_Unpacking_large_integers_from_bytes.py

i = 2
j = i.to_bytes(3, "big")
k = i.to_bytes(2, "little")
# print(j)
# print(len(j))
# print(len(b"\x124V"))
# print(len(b'\x00x'))



data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, "little"))
print(int.from_bytes(data, "big"))

import struct
hi, lo = struct.unpack(">QQ", data)
print(hi)
print(lo)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, "big"))
print(x.to_bytes(4, "little"))

x = 523 ** 23
print(x)

try:
    x.to_bytes(16, "little")
except OverflowError as e:
    print(e)
finally:
    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1
    print(x.to_bytes(nbytes, "little"))