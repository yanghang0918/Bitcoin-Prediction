def binarySearchRecursive(list_, low, high, key):
    if (low > high):
        return -1
    mid = (low + high) //2
    if (key < list_[mid]):
        return binarySearchRecursive(list_, low, mid - 1, key)
    elif (key > list_[mid]):
        return binarySearchRecursive(list_, mid + 1, high, key)
    else:
        return mid


print(binarySearchRecursive([1,2,3,4,5,6,7], 1, 7, 7 ))