t=int(input()) 

for _ in range(t):
  n=int(input()) 
  arr=list(map(int,input().split(" "))) 

  zeros=ans=0
  for ele in arr:
    if ele==1:
      ans=max(zeros,ans)
      zeros=0
    else:
      zeros+=1  
  ans=max(zeros,ans) 
  print(ans)