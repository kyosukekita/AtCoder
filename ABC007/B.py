c=input()

if c=="a":
  print(-1)
  exit()

last=c[-1]   
if last=="a":
  print(c[:-1])
  exit()

print(c[:-1]+chr(ord(last)-1))
