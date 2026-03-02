def solve():
    n = int(input())
    a = list(map(int,input().split()))

    hasOdd = any(num%2==1 for num in a)
    hasEven = any(num%2==0 for num in a)

    if hasOdd and hasEven:
        a.sort()
    
    print(*a)

solve()