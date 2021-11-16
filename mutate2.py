def mutates(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    count = 0
    if (l2>=l1 and l2<=l1+1) or (l2<=l1 and l2>=l1-1):
        for i in str2:
            if i in str1:
                count += 1
    if count >= l1-2:
        print("nearly equal")
    else:
        print("Different")

str1 = input("Enter the main string :")
str2 = input("Enter the sub string :")
mutates(str1,str2)
