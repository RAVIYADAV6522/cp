t=int(input()) 

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))  

  subArray=0
  i=0
  while i < n:
    if a[i]!=0:
      start=i
      while start<n and a[start]!=0:
        start+=1 
      subArray+=1  
      i=start
    else:
      i+=1  
  
  if subArray==0:
    print(0) 
  elif subArray ==1:
    print(1) 
  else:
    print(2)



        



