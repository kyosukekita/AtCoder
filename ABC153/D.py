H=int(input())

def attack(n):
    if n==1:
        return 1
    else:
        return 2*attack(int(n/2))+1

attack(H)
