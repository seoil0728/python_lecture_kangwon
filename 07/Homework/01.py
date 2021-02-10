
def readFile(path):
    with open(path,"r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path,"a") as f:
        return f.write(contents)

def countWord(path):
    count = 0
    s = readFile(path)
    t = s.replace(",", "")
    for word in t.split(" "):
        if(not word.isdigit()):
            count += 1

    return count

def countSentence(path):
    count = 0
    s = readFile(path)
    for i in range(len(s)):
        if(s[i] == "." or s[i] == "!" or s[i]=="?"):
            count += 1

    return count

def findLongestWord(path):
    max = ""
    s = readFile(path)
    for word in s.split(" "):
        if(len(word) > len(max)):
            max = word

    return max

def findShortestWord(path):
    mini = findLongestWord(path)
    s = readFile(path)
    for word in s.split(" "):
        if(len(mini) > len(word)):
            mini = word

    return mini



print("Number of words: " + str(countWord("about KNU.txt")))
print("Number of sentence: " + str(countSentence("about KNU.txt")))
print("Longest word: " + findLongestWord("about KNU.txt"))
print("Shortest word: " + findShortestWord("about KNU.txt"))

re = writeFile("result.txt", "Number of words: " + str(countWord("about KNU.txt")) + "\n")
re = writeFile("result.txt", "Number of sentence: " + str(countSentence("about KNU.txt")) + "\n")
re = writeFile("result.txt", "Longest word: " + findLongestWord("about KNU.txt") + "\n")
re = writeFile("result.txt", "Shortest word: " + findShortestWord("about KNU.txt") + "\n")
