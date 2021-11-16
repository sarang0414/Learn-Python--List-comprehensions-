import array

r = 3
c = 4
multi_arr = [[0 for j in range(c)] for i in range(r)]
print(multi_arr)
for i in range(r):
    for j in range(c):
        multi_arr[i][j] = j
print(multi_arr)