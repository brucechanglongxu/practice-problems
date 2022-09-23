def UniquePathHelper(i, j, r, c, A, paths):
    # boundary condition or constraints
    if (i == r or j == c):
        return 0
 
    if (A[i][j] == 1):
        return 0
 
    # base case
    if (i == r - 1 and j == c - 1):
        return 1
 
    if (paths[i][j] != -1):
        return paths[i][j]

    paths[i][j] = UniquePathHelper(
        i + 1, j, r, c, A, paths) + UniquePathHelper(i, j + 1, r, c, A, paths)
    return paths[i][j]
