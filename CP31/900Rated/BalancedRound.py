t=int(input()) 

for _ in range(t):
  n,k=map(int,input().split())
  a=list(map(int,input().split()))  
  
  c=ans=1
  a.sort()
  for i in range(1,n):
    if a[i]-a[i-1] <=k:
      c+=1
      ans=max(ans,c) 
    else:
      c=1 
  print(n-ans)
