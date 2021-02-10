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
print("          a  = ",a)
b = transpose(a)
print("Transpose(a) = ",b)