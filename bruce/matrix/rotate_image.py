def rotateMatrix(mat):
    # reversing the matrix
    for i in range(len(mat)):
        mat[i].reverse()
    # make transpose of the matrix
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            # swapping mat[i][j] and mat[j][i]
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
 
 
# Function to print the matrix
def displayMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()
