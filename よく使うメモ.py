# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
#リスト入力
c=list(map(int,input().split()))
S = [input() for _ in range(N)]
#2次元配列入力
s=[list(map(int,list(input().split()))) for _ in range(h)]
# 出力
print("{} {}".format(a+b+c, s))

#再帰
import sys
sys.setrecursionlimit(10**6)


#eエラトステネスのふるい n以下の素数をリストで返す
def get_sieve_of_eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)
   
   
#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table


#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1
    
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
    
    
#xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res
    

import itertools
L = [0, 1] #生成する数字
num = 3 #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))

'''実行結果
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
'''


