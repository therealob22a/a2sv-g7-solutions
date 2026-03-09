n,t=map(int,input().split())
a=list(map(int,input().split()))

# Sliding window algo

sol=0

total=0
i=0
for j in range(n):
    total+=a[j]
    while total>t:
        total-=a[i]
        i+=1
    sol=max(sol,j-i+1)

print(sol)
