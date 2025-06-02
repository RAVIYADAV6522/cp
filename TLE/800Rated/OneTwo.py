t=int(input()) 

for _ in range(t):
  n=int(input())
  arr=list(map(int,input().split(" "))) 
  
  
  def helper(arr):
    twos=arr.count(2) 
    start=0
    for i in range(len(arr)):
      if arr[i]==2:
        start+=1 
        if start==twos-start:
          return i+1 
      else:
        if start==twos-start:
          return i+1  
    return -1 
  print(helper(arr))


