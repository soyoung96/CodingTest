import sys

money = 1000-int(sys.stdin.readline().rstrip()) #거스름돈


subMoney=[500,100,50,10,5,1]

answer=0;

for subMoneyElt in subMoney: #O(n)
    while(money>=subMoneyElt):
        money-=subMoneyElt
        answer+=1
print("{0}".format(answer))







