t=int(input()) 

for _ in range(t):
  n,k=map(int,input().split())
  s=input() 

  mapp={} 
  for char in s:
    if char not in mapp:
      mapp[char]=1 
    else:
      mapp[char]=mapp[char]+1 
  
  count=0
  for value in mapp.values():
    if value%2==1:
      count+=1 
  
  if count-k>1:
    print("No") 
  else:
    print("Yes")
