# Uses python3
# coding=utf-8
import sys

tokens = input()

tokens = tokens.split()

try:
    a = int(tokens[0])
    b = int(tokens[1])
except ValueError:
    print('Enter valid numbers')
    sys.exit(0)

if 0 <= a <= 9 and 0 <= b <= 9:
    print(a + b)
else:
    print('Numbers not satisfying constraints: 0 ≤ a,b ≤ 9')
