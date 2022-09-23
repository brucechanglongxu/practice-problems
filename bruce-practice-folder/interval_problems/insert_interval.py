def mergeInterval2(arr, n, newPair) :
    # Create stack of type
    # pair<int, int>
    stk = []
    # Pushing first pair
    stk.append(arr[0])
    # Storing the top element
    top = stk[len(stk) - 1]
    # Checking is newPair.first
    # is less than top.second
    if (newPair[0] < top[1]) :
        # Pop the top element
        # as it will merge with the
        # previous range
        stk.pop()
        # Re-assigning top.first
        top[0] = min(top[0], newPair[0])
        # Re-assigning top.second
        top[1] = max(top[1], newPair[1])
        # Push the current interval
        stk.append(top)
    else :
        # Push the new pair as it does
        # not intersect to first pair
        stk.append(newPair)
    # Iterate i from 1 to n - 1
    for i in range(1, n) :
        # Store the top element of
        # the stack stk
        top = stk[len(stk) - 1]
        # Checking is arr[i].first
        # is less than top.second
        if (arr[i][0] < top[1]) :
            # Pop the top element
            # as it will merge with the
            # previous range
            stk.pop()
            # Re-assigning top.first
            top[0] = min(top[0], arr[i][0])
            # Re-assigning top.second
            top[1] = max(top[1], arr[i][1])
            # Push the current interval
            stk.append(top)
        else :
            # Push the new pair as it does
            # not intersect to first pair
            stk.append(arr[i])
    # Storing the final intervals
    finalIntervals = []
    # Popping the stack elements
    while (len(stk) > 0) :
        ele = stk[len(stk) - 1]
        stk.pop()
        # Push ele in finalIntervals
        finalIntervals.append(ele)
    # Displaying the final result
    while (len(finalIntervals) > 0) :
        ele = finalIntervals[len(finalIntervals) - 1]
        finalIntervals.pop()
        print(ele[0] , end = ", ")
        print(ele[1])
