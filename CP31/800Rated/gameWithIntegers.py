t=int(input()) 
for _ in range(t):
  n=int(input()) 

  vanya=False
  while(True):
    if n%3==1 or n%3==2:
      vanya=True 
      break 
    else:
      
      break
  if vanya:
    print("First") 
  else:
    print("Second")
