import math

def sumNodes(l):

    leafNodeCount = math.pow(2, l - 1)

    sumLastLevel = 0

    sumLastLevel = leafNodeCount * (leafNodeCount + 1) / 2

    sum = sumLastLevel * l

    return int(sum)

l = 3;
print (sumNodes(l));
