S, T = input().split()
A, B = map(int, input().split())
U=input()

if U==S:
    A -=1
    print(A,B)
else:
    B-=1
    print(A,B)