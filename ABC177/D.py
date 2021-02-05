#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]


N,M = map(int, input().split())
AB=[list(map(int,list(input().split()))) for _ in range(M)]

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N

for ab in AB:
  unite(ab[0]-1,ab[1]-1)

tank=set([]) #len(tank)はグループの数
for i in range(N):
  tank.add(find(i))
print(max([abs(i) for i in par if i <0] ))#一番大きなグループのサイズを答える
