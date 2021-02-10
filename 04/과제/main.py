def calculateScore(year, math, science, programming):
  if (year == 1):
    return (math+science)/2
  elif (year == 2):
    return (math+programming)/2
  elif (year == 3):
    return (math+science+programming)/3
  else:
    if(math >= science and math >= programming):
      return math
    else:
      if(science >= programming):
        return science
      else:
        return programming

print(calculateScore(1,100,95,90))
print(calculateScore(2,100,95,90))
print(calculateScore(3,100,95,90))
print(calculateScore(4,100,95,90))