def transpose(row,matrix,col):
    for i in range(row):
        for j in range(0, i):
            matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end =" ")
        print()

matrix=[]
row=int(input())
column=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))
transpose(row,matrix,column)