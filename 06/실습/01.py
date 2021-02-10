import string

def Is_num_symbol(str):
    res = ""
    for n in range(len(str)):
        if(str[n] in string.digits or str[n] in string.punctuation):
            res += str[n]
    return res

sts = input("your string : ")
print(Is_num_symbol(sts))