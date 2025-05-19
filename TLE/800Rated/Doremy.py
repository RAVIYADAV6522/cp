t=int(input()) 

for _ in range(t):
  n=int(input()) 
  arr=list(map(int,input().split(" "))) 

  def helper():
    map={} 
    for i in range(len(arr)):
      if arr[i] not in map:
        map[arr[i]]=1 
      else:
        map[arr[i]]+=1  
    
    if len(map)>2:
      return "No" 
    elif len(map)==1:
      return "Yes" 
    else:
      frequency=list(map.values())
      diff = abs(frequency[0]-frequency[1]) 
      if diff ==0 or diff ==1:
        return "Yes" 
      else:
        return "No" 
  
  print(helper())
