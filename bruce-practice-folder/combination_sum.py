def combinationSum(arr, sum):
    ans = []
    temp = []
 
    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans
 
def findNumbers(ans, arr, temp, sum, index):
     
    if(sum == 0):
         
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return
       
    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):
 
        # checking that sum does not become negative
        if(sum - arr[i]) >= 0:
 
            # adding element which can contribute to
            # sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
 
            # removing element from list (backtracking)
            temp.remove(arr[i])
