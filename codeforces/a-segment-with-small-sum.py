def solve():
    n,s=map(int,input().split())
    a=list(map(int,input().split()))

    left=0
    sum=0
    length = 0
    for right in range(n):
        sum+=a[right]
        while sum>s:
            sum-=a[left]
            left+=1
        length=max(length,right-left+1)
    
    print(length)


solve()
