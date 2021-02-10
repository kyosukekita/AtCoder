import sys
sys.setrecursionlimit(10**6)
import math

X=int(input())

ans=0
money=100
while(money<X):
  money+=(money)//100 #ここを//ではなく、/にすると、after contestがWAになる
  ans+=1

print(ans)
