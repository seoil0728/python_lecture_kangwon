import random

def Question_num():
  answer = random.randint(1,20)
  count = 0
  print("Random Game Start!")
  while(True):
    number = int(input("Enter answer Number (1~20): "))
    count += 1
    if(number == answer):
      break
    else:
      if(number<answer):
        print("your num is small!")
      else:
        print("your num is big!")
      continue
  print("your num is correct!")
  print("I have",count,"th challenge")
    
Question_num()