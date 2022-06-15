
def solve():
    
    t = int(input())
    
    for _ in range(t):
        
        n,a,b = map(int,input().split())
        
        result = (360+(2*n)) - (a+b)
        
        print(result)
        


if __name__=="__main__":
    
    solve()