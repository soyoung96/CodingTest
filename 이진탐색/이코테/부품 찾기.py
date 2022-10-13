import sys

n = int(sys.stdin.readline())
inputN = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
inputM = list(map(int,sys.stdin.readline().split()))

inputN.sort() #O(10^6)-> OK

def binarySearch(listParam,target,start,end):
    while(start<=end):
        mid = (start+end)//2
        if(listParam[mid]==target):
            return mid
        elif(target<listParam[mid]):
            end = mid-1
        else:
            start = mid+1
    
    return None

for i in inputM:
    ans = binarySearch(inputN,i,0,len(inputN)-1)
    if(ans != None):
        print("yes",end=" ")
    else:
        print("no",end=" ")


