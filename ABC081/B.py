def main(n):
	ans = 0
	while n % 2 == 0:
		n = n/2
		ans += 1
	return ans
 
n = int(input())
a = map(int, input().split())
ans = min(map(main, a))
print(ans)
