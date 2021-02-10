def isPalindrome(str):
    reStr = ""
    for i in range(len(str)-1, -1, -1):
        reStr += str[i]
    return str == reStr

val = input("Input your word : ")
if(isPalindrome(val)):
    print("your word " + val + " is Palindrome")
else:
    print("not Palindrome")