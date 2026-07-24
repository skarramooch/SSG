from enum import Enum

class Color(Enum):
    RED = 'red'

c = Color.RED
print(c)
print(c == 'red')
print(c == Color.RED)
print(str(c))
