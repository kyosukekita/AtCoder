x, n = map(int, input().split())
a = [int(x) for x in input().split()]
b = [i for i in range(0,102) if i not in a] 
b_tmp = list(map(lambda s:abs(s-x), b)) #b_tmpはbとxの差分のリストをさくせい
address = b_tmp.index(min(b_tmp))
print(b[address])
