import sys

a = input()

print(a)
print(sys.argv)

if len(sys.argv) < 2:
    sys.exit(1)

print('END')