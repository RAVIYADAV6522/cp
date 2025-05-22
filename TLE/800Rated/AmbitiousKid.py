
N=int(input()) 
arr=list(map(int,input().split(" ")))
ans=float('inf')
for i in range(N):
  ans=min(abs(arr[i]),ans) 
print(ans)

