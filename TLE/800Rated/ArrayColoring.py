t=int(input()) 

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split(" "))) 

  oddCount=0
  for i in a:
    if i%2!=0:
      oddCount+=1 
    
  if oddCount%2==0:
    print("Yes") 
  else:
    print("No")
