t=int(input()) 

for _ in range(t):
  a,b,n=map(int,input().split(" "))
  arr=list(map(int,input().split(" "))) 
  
  ans=0
  for i in arr:
    ans+=min(i,a-1) 
  print(ans+b) 
