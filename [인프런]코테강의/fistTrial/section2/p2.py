T = input("")
T = int(T)
for i in range(T):
  N,s,e,k = map(int,input("").split())
  temp = list(map(int,input("").split()))
  temp = temp[s-1:e]
  temp.sort()
  print("#{} {}".format(i+1,temp[k-1]))
  
  
  
  
    
