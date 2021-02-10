def Is_same_place(str1, str2):
    if (len(str1) > len(str2)):
        str1, str2 = str2, str1
    for i in range(len(str1)):
        if(str1[i] == str2[i]):
            print(str1[i] + " is at " + str(i))

sts1 = input("Enter your first string : ")
sts2 = input("Enter your second string : ")

print()
Is_same_place(sts1,sts2)