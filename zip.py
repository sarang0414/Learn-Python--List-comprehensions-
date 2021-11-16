data1 = ["abc","def","ghi"]
data2 = [1,2,3]

result = [(i,j) for i,j in zip(data2,data1)]
print(result)