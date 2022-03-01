# n,k = map(int,input("").split(" "))

# temp=[]
# for i in range(1,n+1):
#   if (n % i ==0):
#     temp.append(i)

# print(sorted(temp)[k-1])

#v풀이
n,k = map(int,input("").split(" "))

cnt =0
for i in range(1,n+1):
  if (n % i ==0):
    cnt+=1
  if cnt ==k:
    print(i)
    break
else:
  print(-1)