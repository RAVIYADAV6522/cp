t=int(input()) 

for _ in range(t):
  start,n = map(int,input().split())  

  x0=0 
  if n%4==0:
    finalPos=0  
  elif n%4==1:
    finalPos=-n 
  elif n%4==2:
    finalPos=1 
  else:
    finalPos=n+1 
  
  if start%2==0:
    finalPos = start + finalPos 
  else:
    finalPos = start - finalPos  
  
  print(finalPos)

