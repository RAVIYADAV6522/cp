t=int(input()) 

for _ in range(t):
  n=int(input())
  s=input() 
  
  count=1
  maxC=0
  for i in range(1,len(s)):
    if s[i]==s[i-1]:
      count+=1 
      
    else:
      maxC=max(count,maxC)  
      count=1 
  maxC=max(count,maxC) 
  print(maxC + 1 )
  


    

    


