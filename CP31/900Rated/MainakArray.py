t=int(input()) 

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))  

  ans=a[-1]-a[0] 
  
  # case 1 : a1 is fixed
  for i in range(1,len(a)):
    ans=max(ans,a[i]-a[0]) 
  
   # case 2 : a5 is fixed
  for i in range(0,len(a)-1):
    ans=max(ans,a[-1]-a[i])  
  
   # case 3 : both are not fixed
  for i in range(len(a)-1):
    ans=max(ans,a[i]-a[i+1])  
  
  print(ans)