t=int(input()) 

for _ in range(t):
  n=int(input()) 
  arr=list(map(int,input().split(" "))) 

  
  def helper():
    copy=arr[:] 
    if sorted(copy)==arr:
      return "Yes" 
    for i in range(n-1):
      for j in range(1,n-1):
        if arr[j-1]<arr[j] and arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j] 
    arr2=arr[:] 
    if sorted(arr2)==arr:
      return "Yes" 
    else:
      return "No"
  print(helper()) 
