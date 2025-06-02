t=int(input()) 

for _ in range(t):
  n=int(input()) 
  a=list(map(int,input().split(" "))) 

  def helper(a):
    if len(a)==1:
      return 0 
    
   
    ops=0
    for end in range(len(a)-1):
      if a[end]%2==a[end+1]%2:
        ops+=1
      
    return ops 
  
  print(helper(a))