def transpose(a):

    b = []
    col = 0
    while(col < len(a[0])):
        colList = []
        for i in range(len(a)):
            colList += [a[i][col]]
        col += 1
        b += [colList]


    return b


a = [[1,2,3,4],[5,6,7,8]]

b = transpose(a)
print(b)

'''




[[1,2,3,4],[5,6,7,8]] # [[1,5],[2,6],[3,7],[4,8]]
# 00,10 01,11 02,12 03,13

row = 2
col = 4

b[j].append(a[i][j])

b[0] = [1,5]
b[i] = [a[i]
b[0].append(a[1,5])
b[i] = 
 a[0][0]
'''