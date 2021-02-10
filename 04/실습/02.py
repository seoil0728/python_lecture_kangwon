def cal_Electricity(usage,grade):
  if(usage<0):
    print("Usage Error")
  else:
    if(grade == 1):
      print("Your amount is",round(535*usage +  (535*usage*0.03),2))
    elif(grade == 2):
      print("Your amount is",round(377*usage + (377*usage*0.03),2))
    elif(grade == 3):
      print("Your amount is",round(291*usage + (291*usage*0.03),2))
    else:
      print("No such grade")

eUsage = int(input("electricity usage : "))
grade = int(input("grade : "))
cal_Electricity(eUsage,grade)
