t=int(input()) 

for _ in range(t):
  n,k,x=map(int,input().split()) 
  
  minSum=k*(k+1)//2 
  MaxSum=(n*(n+1)//2) - ((n-k)*(n-k+1)//2)
  
  if x>=minSum and x<=MaxSum:
    print("Yes") 
  else:
    print("No") 