t=int(input()) 

for _ in range(t):
  s=input() 

  Ones=Zeors=0 
  for ch in s:
    if ch=="0":
      Zeors+=1 
    elif ch=="1":
      Ones+=1 
  
  tLen=0
  for ch in s:
    if ch=="0" and Ones>0:
      Ones-=1 
      tLen+=1 
    elif ch=="1" and Zeors>0:
      Zeors-=1
      tLen+=1 
    else:
      break 
  
  print(len(s)-tLen)
