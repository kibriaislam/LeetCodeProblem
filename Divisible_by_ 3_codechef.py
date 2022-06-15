"""
commented one will get time limit exceed but this one is right for greedy aproach 
"""

# def solve():
    
#     t = int(input())
    
    
#     for _ in range(t):
        
#         a , b = map(int, input().split())
        
#         if a%3 == 0 or b%3==0:
#             print(0)
#         else:
            
#             x = min(a,b)
#             y = abs(a-b)
#             cnt = 0
            
#             while(True):
#                 cnt += 1
#                 if y%3==0:
#                     print(cnt)
#                     break
#                 y = abs(a-y)
#     return


def solve():
    
    t = int(input())
    
    
    for _ in range(t):
        
        a , b = map(int, input().split())
        
        if a%3 == 0 or b%3==0:
            print(0)
        elif (a%3 == b%3):
            print(1)
        else:
            print (2)
    return


if __name__ == "__main__":
    
    solve()
              