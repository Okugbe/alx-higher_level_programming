#!/usr/bin/python3
for item in range(ord('a'), ord('z') + 1):
    if chr(item) == 'q' or chr(item) == 'e':
        continue
    print('{:c}'.format(item), end='')
