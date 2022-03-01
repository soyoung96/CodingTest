# n = int(input())
# list1 = list(map(int,input().split()))

# m = int(input())
# list2 = list(map(int,input().split()))

# resultList = sorted(list1+list2)
# # sort()=> nlogn => 8log8
# #이미 정렬되어 있는것을 활용해서 합쳐서 정렬=>8번

# for i in resultList:
#   print(i , end=" ")

n = int(input())
list1 = list(map(int,input().split()))

m = int(input())
list2 = list(map(int,input().split()))

list3 = [0]*(len(list1)+len(list2))
ptr1 = 0
ptr2 = 0
for i in range(len(list3)):
  if(list1[ptr1]<list2[ptr2]):
    list3[i] = list1[ptr1]
    ptr1+=1
    if(ptr1==len(list1)):
      list3[i+1:] = list2[ptr2:]
      break
  else:
    list3[i] = list2[ptr2]
    ptr2+=1
    if(ptr2==len(list2)):
      list3[i+1:] = list1[ptr1:]
      break
    
for i in list3:
  print(i , end=" ")

