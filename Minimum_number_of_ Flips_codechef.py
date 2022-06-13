
def solve():
    t = int(input())
    for _ in range(t):
        size = int(input())
        arr = list(map(int,input().split()))
        
        if size%2 != 0 :
            print(-1)
        elif sum(arr)==0:
            print(0)
            
        else :
            x =sum(arr)//2
            print(x)



solve()