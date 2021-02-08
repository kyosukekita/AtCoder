N, K = map(int, input().split())
A = list(map(int, input().split()))
 
town = 1
visited = [town]
 
flag = [0] * N
flag[0] = 1
 
for _ in range(K):
  town = A[town-1]
  if not flag[town-1]:
    flag[town-1] = 1
    visited.append(town)
  else:
    break

s = visited.index(town)
cycle = visited[s:]
print(cycle[(K-s) % len(cycle)])



#3/57がTLEになる
N,K=map(int,input().split())
A=list(map(int,input().split()))
A=[i-1 for i in A]#すべての要素の数を1減らしておく

repeat=[] #繰り返しの部分
seen=[False for _ in range(N)]#既にみたことがあったかどうか
current=0 #今0(町1)にいる。

while True:
  if seen[current]==True:#一度通った頂点を見つけたとき
    while (repeat[0]!=current):
      K-=1
      repeat.pop(0)
      
      if K==0:
        break
    break
   #最初は愚直にシミュレーションしいく
  repeat.append(current)#繰り返しの部分
  seen[current]=True
  current=A[current]

print(repeat[K%len(repeat)]+1)
