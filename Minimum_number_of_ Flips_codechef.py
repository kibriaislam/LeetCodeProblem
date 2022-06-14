
def solve():
    t = int(input())
    for _ in range(t):
        size = int(input())
        arr = list(map(int,input().split()))
        
        x = arr.count(1)
        y = arr.count(-1)
        
        if (size%2 != 0):
            print(-1)
        else:
            
            z = max(x,y)
            
            print(z - (size//2))



solve()