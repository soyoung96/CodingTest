import sys

inStr = str(sys.stdin.readline().rstrip())
alphas = ''
allSum =0
for inStrElt in inStr:
    if(inStrElt.isalpha()):
        alphas+=inStrElt
    else:
        allSum+=int(inStrElt)

if(allSum==0):
    allSum=''

print(''.join(sorted(alphas))+str(allSum))