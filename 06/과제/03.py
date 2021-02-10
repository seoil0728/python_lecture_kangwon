import string

def countAlphabet(x):
    res = 0
    for c in x:
        if(c.isalpha()):
            res += 1
    return res

def countAlphabet2(x):
    count = 0
    a = string.ascii_letters
    for i in range(len(x)):
        if(x[i] in a):
            count += 1
    return count


sentence = input("Enter Sentence : ")
print(countAlphabet(sentence))
print(countAlphabet2(sentence))