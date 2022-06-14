from math import ceil

def solved():
    t = int(input())
    
    for _ in range(t):
        
        n, x = map(int,input().split())

        print(ceil((n/6))*x)



if __name__ == "__main__":
    solved()