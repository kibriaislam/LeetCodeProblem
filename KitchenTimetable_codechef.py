def solve():
    t = int(input())
    
    for _ in range(t):
        
        n = int(input())
        
        a = [ int(i) for i in input().split()]
        b = [ int(i) for i in input().split()]
        
        cnt = 0
        if a[0]>=b[0]:
            cnt+=1
        for i in range(len(a)-1):
            if(abs(a[i]-a[i+1]))>=b[i+1]:
                cnt+=1
        print(cnt)
    return 0


solve()