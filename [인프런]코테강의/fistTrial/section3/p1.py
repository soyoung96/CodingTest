n = int(input())
strList=list()
for i in range(n):
  str = input()
  strList.append(str)

for i in range(len(strList)):
  tmpStr = strList[i]
  lenStr=len(tmpStr)
  for j in range((lenStr)//2):
    if(tmpStr[j].lower() ==tmpStr[lenStr-1-j].lower()):
      continue
    else:
      print("#%d NO"%(i+1))
      break
  else:#break 안되고 정상 종료
    print("#%d YES"%(i+1))
    