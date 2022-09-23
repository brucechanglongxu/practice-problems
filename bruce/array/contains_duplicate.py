def checkDuplicatesWithinK(arr,  n,  k):
 
    # traversing the input array
    for i in range(n):
        j = i + 1
        range_ = k
         
        # searching in next k-1 elements if its duplicate
        # is present or not
        while (range_ > 0 and j < n):
            if (arr[i] == arr[j]):
                return True
            j += 1
            range_ -= 1
 
    return False
 
