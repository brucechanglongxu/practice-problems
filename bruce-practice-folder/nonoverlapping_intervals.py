def findFreeinterval(arr, N):
    # If there are no set of interval
    if N < 1:
        return
    # To store the set of free interval
    P = []
    # Sort the given interval according
    # Starting time
    arr.sort(key = lambda a:a[0])
    # Iterate over all the interval
    for i in range(1, N):
        # Previous interval end
        prevEnd = arr[i - 1][1]
        # Current interval start
        currStart = arr[i][0]
        # If Previous Interval is less
        # than current Interval then we
        # store that answer
        if prevEnd < currStart:
            P.append([prevEnd, currStart])
     
    # Print the intervals
    for i in P:
        print(i)
