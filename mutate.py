def mutate(str1,str2):
    count = 0
    for i in str2:
        if i in str1:
            count += 1
    if count >= len(str1)/1.5:
        print("The string is nearly equal")
    else:
        print("The string is not nearly equal")

str1 = input("Enter the main string :")
str2 = input("Enter the sub string :")

mutate(str1,str2)