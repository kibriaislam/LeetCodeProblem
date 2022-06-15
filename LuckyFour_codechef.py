
def solve():
    t = int(input())
    for _ in range(t):
        cnt= 0
        a = int(input())
        
        if a == 0 :
            print(0)
        else:
            while(a>0):
                temp = a%10
                if temp == 4:
                    cnt += 1
                a =a//10
            print(cnt)
    return 0   

solve()