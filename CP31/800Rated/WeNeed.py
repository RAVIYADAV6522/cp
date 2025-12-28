t=int(input())

for _ in range(t):
  n=int(input())
  a=list(map(int,input().split(" "))) 
  ans=0
  for ele in a:
      ans^=ele  
  
  if len(a)%2==0:
      if ans==0:
        print(ans) 
      else:
         print(-1) 
  else:
    print(ans)
