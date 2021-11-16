def even_num(n):
    if n%2==0:
        return True
    else:
        return False

data = filter(even_num,[x for x in range(1,10)])
print(list(data))