sx,sy,tx,ty=map(int,input().split())
x=tx-sx
y=ty-sy

path="U"*y+"R"*x+"D"*y+"L"*(x+1)+"U"*(y+1)+"R"*(x+1)+"D"+"R"+"D"*(y+1)+"L"*(x+1)+"U"
print(path)
