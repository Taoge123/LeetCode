# Python Program to get the maximum
# possible integer from given array
# of integers...

# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return cmp(int(ba), int(ab))


# driver code 
a = [54, 546, 548, 60, ]
sorted_array = sorted(a, cmp=comparator)
number = "".join([str(i) for i in sorted_array])
print(number)