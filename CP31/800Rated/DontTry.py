t=int(input()) 

for _ in range(t):
  n,m=map(int,input().split(" ")) 
  x=input() 
  s=input() 
  
  

  repeated=x 
  ans=-1 
  for i in range(6):
    if s in repeated:
      ans=i 
      break 
    repeated+=repeated 
  print(ans)
    


