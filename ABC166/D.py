X=int(input())
#ＡもBも実は、-200~200くらいまで探索したらいい

ans=False
for a in range(-200,201):
  for b in range(-200,201):
    if pow(a,5)-pow(b,5)==X:
      print(a,b)
      ans=True
      break
  
  if ans:
    break
