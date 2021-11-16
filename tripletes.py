n = int(input("Enter the limit :"))
tripletes = [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a*a + b*b == c*c]
print(list(tripletes))

def trip():
    result = []

    for a in range(1,25):
        for b in range(a,25):
            for c in range(b,25):
                if a*a + b*b == c*c:
                    data = []
                    data.append(a)
                    data.append(b)
                    data.append(c)
                    result.append(data)
    print(result)
trip()