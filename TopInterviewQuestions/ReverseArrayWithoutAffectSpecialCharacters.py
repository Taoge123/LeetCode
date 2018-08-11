def isAlphabet(x):
    return x.isalpha()

def reverse(string):
    LIST = toList(string)

    r = len(LIST) - 1
    l = 0

    while l < r:
        if not isAlphabet(LIST[l]):
            l += 1
        elif not isAlphabet(LIST[r]):
            r -= 1

        else:
            LIST[l], LIST[r] = swap(LIST[l], LIST[r])
            l += 1
            r -= 1

    return toString(LIST)


def toList(string):
    LIST = []
    for i in string:
        LIST.append(i)
    return LIST

def toString(LIST):
    return ''.join(LIST)

def swap(a, b):
    return b, a



string = "a!!!b.c.d,e'f,ghi"
print("Input string: " + string)
string = reverse(string)
print("Output string: " + string)

