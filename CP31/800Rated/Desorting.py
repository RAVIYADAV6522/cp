t=int(input()) 

for _ in range(t):
  n=int(input()) 
  a=list(map(int,input().split(" "))) 

  copy=a[:] 
  copy.sort() 

  def helper(copy,a):
    if copy!=a:
      return 0
    
    ans=float('inf')
    for i in range(1,len(a)):
      diff=((a[i] - a[i-1])//2)  + 1
      ans=min(ans,diff)

    return ans
  print(helper(copy,a)) 


