# n = int(input())

# cnt =0
# for h in range(n+1):
#   for m in range(60):
#     for s in range(60):
#       strS = "%2d"%s
#       strM = "%2d"%m
#       strH = "%2d"%h
#       if(strS[0]=="3" or strS[1]=="3"):
#         cnt+=1
#       elif(strM[0]=="3" or strM[1]=="3"):
#         cnt+=1
#       elif(strH[0]=="3" or strH[1]=="3"):
#         cnt+=1

# print(cnt)

n = int(input())

cnt =0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if("3" in str(h)+str(m)+str(s)):
        cnt+=1
        
print(cnt)
        
      
      