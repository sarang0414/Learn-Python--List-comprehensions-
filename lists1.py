data = [(x,y) for x in range(0,5) for y in range(0,5) if (x+y)%2==0]
print(data)

def square(n):
    return n*n
new_data = map(square,[1,2,3,4])
print(list(new_data))


print("Hello Userss")