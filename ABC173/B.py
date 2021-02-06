from collections import defaultdict
N=int(input())

d=defaultdict(int)
for i in range(N):
  c=input()
  if c=="AC":
    d["AC"]+=1
  elif c=="WA":
    d["WA"]+=1
  elif c=="TLE":
    d["TLE"]+=1
  else:
    d["RE"]+=1
    
print("AC x "+str(d["AC"]))
print("WA x "+str(d["WA"]))
print("TLE x "+str(d["TLE"]))
print("RE x "+str(d["RE"]))
  
