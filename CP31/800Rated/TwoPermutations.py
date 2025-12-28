t=int(input()) 

for _ in range(t):
  n,a,b=map(int,input().split(" ")) 

  if a==b==n:
    print("Yes") 
  elif a+b < n-1:
    print("yes") 
  else:
    print("No") 
  