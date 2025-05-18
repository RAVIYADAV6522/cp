t=int(input()) 

for _ in range(t):
  n,x=map(int,input().split(" ")) 
  arr=list(map(int,input().split(" ")))
  
  d1=arr[0]
  dN=2*(x-arr[-1])
  diff=0
  for i in range(1,len(arr)):
    diff=max(diff,arr[i]-arr[i-1]) 
  print(max(d1,dN,diff)) 
  

   
    