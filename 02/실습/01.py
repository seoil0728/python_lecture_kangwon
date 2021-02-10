val = input("값을 입력해주세요(n>3600) : ")
val = int(val)

hour = int(val/3600)
minute = int((val%3600)/60)
sec = int(val%60)

print(hour,"시간",minute,"분",sec,"초")