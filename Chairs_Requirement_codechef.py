def solved():
    t = int(input())
    for _ in range(t):
        
        x, y = input().split()
        
        if int(y)>=int(x):
            print(0)
        else:
            print( int(x)- int(y))
        
        
        
        

if __name__ == "__main__":
    
    solved()