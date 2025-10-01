from package.maths import *
from package.subpackages.math1 import *

## From package.maths import add, subtract, multiply, divide
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

print("-----")

## From package.subpackages.math1 import mod, power
print(mod(10, 5))
print(power(2, 3))