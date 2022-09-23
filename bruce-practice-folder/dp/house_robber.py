def maxLoot(hval,n):
 
    # base case
    if (n < 0):
        return 0
 
    if (n == 0):
        return hval[0]
     
    # if current element is pick then previous cannot be
    # picked
    pick = hval[n] + maxLoot(hval, n - 2)
    # if current element is not picked then previous
    # element is picked
    notPick = maxLoot(hval, n - 1)
 
    # return max of picked and not picked
    return max(pick, notPick)
