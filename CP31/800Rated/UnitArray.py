t=int(input()) 

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split(" "))) 

  plus=neg=0
  for i in a:
    if i >0:
      plus+=1
    else:
      neg+=1 

  ans=0
  while(plus<neg or neg%2==1):
    plus+=1
    neg-=1 
    ans+=1 
  
  print(ans)
  

    
