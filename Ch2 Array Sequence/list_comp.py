print("--- List Comprehension ---")
symbols = "$¢£¥€¤"
codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

print(tuple(ord(symbol) for symbol in symbols))

print("--- Tuples ---")
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)

print(divmod(25, 10))
t = (25, 10)
print(divmod(*t))

quotient, reminder = divmod(*t)
print((quotient, reminder))

import os
import sys
print(__file__)
print(sys.argv[0])

a, b, *rest = range(5)
print((a, b, rest))

print("--- Named Tuples ---")
from collections import namedtuple

City = namedtuple("City", "name country population coordinates")
print(City)

tokyo = City("Tokyo", "JP", 36.933, (35.690, 139.692))
print(tokyo)
taipei = City("Taipei", "TWN", 2.704, (25.02, 121.38))

print(taipei)
print(taipei.population)
print(taipei[1])
print(City._fields)

LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi", "IN", "21.935", LatLong(28.61, 77.20))
print(delhi_data)
delhi = City._make(delhi_data)
print(delhi)
delhi = City(*delhi_data)
print(delhi)

print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ": ", value)
for key, value in taipei._asdict().items():
    print(key + ": ", value)

print("--- Slicing ---")
s = slice(0, 10, 2)
print(s)

print("--- Augmented Assignment ---")
board = [['_'] * 3 for i in range(3)]
print(board)
board[0][2] = 'X'
print(board)
print(id(board[0]))
print(id(board[1]))
print(id(board[2]))

another_board = [['_'] *3] * 3
another_board[0][2] = 'X'
print(another_board)
print(id(another_board[0]))
print(id(another_board[1]))
print(id(another_board[2]))

t = (1, 2, [30, 40])
t[2].extend([50, 60])   
print(t)
