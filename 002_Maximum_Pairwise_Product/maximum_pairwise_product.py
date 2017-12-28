# Uses python3
import sys

list_size = input()
list_values = input()

try:
    assert (len(list_values) == int(list_size))
except AssertionError:
    print('Entered size is not same as length of values.')
    sys.exit(0)
except ValueError:
    print('Enter a valid number for size')
    sys.exit(0)

try:
    list_values = list(map(int, list_values.split()))
except ValueError:
    print('Enter valid numbers')
    sys.exit(0)

max_one = max(list_values)
list_values.remove(max_one)
max_two = max(list_values)

print(max_one * max_two)
