def binsearch(numList,target):
    low ,high= 0,len(numList)-1
    while low<=high:
        mid = (low+high)//2
        if numList[mid]==target:
            return mid
        elif numList[mid]>target:
            high = mid-1
        else:
            low = mid +1
    return -1
print(binsearch([1,2,3,4,5],2))