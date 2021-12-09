#!/usr/bin/env python
# This function divides a by greatest divisible power of b
def max_divide(a, b):
    if a % b != 0:
        return a;

    c = a/b;
    return max_divide(c, b);

# Function to check if a number is ugly or not
def is_ugly(n, args, no):
    if n >= len(args):
        return no == 1

    c = max_divide(no, args[n]);
    return is_ugly(n+1, args, c);


def find_ugly(n, i, count, args):
    if (n < count):
        return i-1

    if is_ugly(0, args, i):
        return find_ugly(n, i+1, count+1, args);
    else:
        return find_ugly(n, i+1, count, args)

def main():
    i = 10
    args = [2,3,5]
    print( "[INPUT] %d" % i)
    output = find_ugly(i, 1, 1, args)
    print( "[OUTPUT] %d" % output)

main()
