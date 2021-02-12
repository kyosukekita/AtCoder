from collections import Counter

n = input()

if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

cnt = Counter(n)

for i in range(112, 1000, 8):
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()

print("No")


#例えば、
#a=Counter("123")
#b=Counter("1234")
#a=Counter({'1': 1, '2': 1, '3': 1})
#b=Counter({'1': 1, '2': 1, '3': 1, '4': 1})
#a-b=Counter()
