t=int(input()) 

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split(" "))) 
  
  b=[] 
  for i in a:
    b.append(n+1-i) 
  print(*b)
