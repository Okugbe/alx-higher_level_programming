#!/usr/bin/python3
for item in range(ord('z'), ord('a') - 1, -1):
    if item % 2 == 0:
        value = 0
    else:
        value = 32
    print('{}'.format(chr(item - value)), end="")
