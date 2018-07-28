def toStringn(List):
    return ''.join(List)

def permute(a, l, r, list1):

    print(str(a) + "----call")
    if l == r:
        # print(toStringn(a))
        list1.append(a)
        print(str(a) + "    result")

    else:
        for i in range(l, r+1):
            print("swap " + str(a[l]) + " " + str(a[i]))
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, list1)
            a[l], a[i] = a[i], a[l]



# Driver program to test the above function
string = "ABC"
list1 = []
n = len(string)
a = list(string)
permute(a, 0, n-1, list1)
print(list1)
