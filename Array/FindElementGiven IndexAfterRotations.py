def findElement(arr, ranges, rotations, index):

    for i in range(rotations - 1, -1, -1):

        #Range[left...right]
        left = ranges[i][0]
        right = ranges[i][1]

        #Rotation will not have any effect
        if (left <= index and right >= index):

            if (index == left):
                index = right
            else:
                index = index - 1

    return arr[index]





