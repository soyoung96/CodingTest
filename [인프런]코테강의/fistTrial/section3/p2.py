inputStr=input()
inputStrLen=len(inputStr)
totalInt=0
for i in range(inputStrLen):
  if(inputStr[i].isdigit()):
    #.isdigot=>2^2까지도 숫자로 인식 .isdecomal=>0-9
    totalInt*=10
    tmpInt=int(inputStr[i])
    totalInt+=tmpInt

numYak=0
for i in range(1,totalInt+1):
  if(totalInt%i ==0):
    numYak+=1

print(totalInt)
print(numYak)
  