import sys

inputL = []
n = int(sys.stdin.readline())
for _ in range(n):
    name,korean,english,math = sys.stdin.readline().split()
    inputL.append([name,int(korean),int(english),int(math)])

inputL.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for name,_,_,_ in inputL:
    print(name)