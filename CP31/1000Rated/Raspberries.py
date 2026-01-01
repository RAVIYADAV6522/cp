t=int(input()) 


for _ in range(t):
  n,k = map(int,input().split()) 
  a=list(map(int,input().split())) 
  
  max_ans=float('inf')
  even_count=0
  for num in a:
    if num%2==0:
      even_count+=1 
    if num%k==0:
      max_ans=0
    
    max_ans=min(max_ans,k-num%k) 
  

  if k==4:
    if even_count>=2:
      max_ans=min(max_ans,0)
    elif even_count==1:
      max_ans=min(max_ans,1) 
    elif even_count==0:
      max_ans=min(max_ans,2) 
  
  print(max_ans) 

   
  
  ### logic goes here -------- [1 5 9]
  
  
  


  
  