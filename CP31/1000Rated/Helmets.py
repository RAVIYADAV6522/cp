t=int(input()) 
for _ in range(t):
  n,p=map(int,input().split()) 
  a=list(map(int,input().split())) 
  b=list(map(int,input().split()))  
  
  ## creating tuple to store both values -----
  v=[] 
  for i in range(n):
    v.append((b[i],a[i])) 
  
  ## sort so that minimum price comes first -----
  v.sort() 
  
  min_cost = p
  already_shared = 1 

  for share_cost , can_be_shared in v:
    if share_cost >= p :
      break 

    if already_shared + can_be_shared >= n:
      min_cost += (n-already_shared) * share_cost 
      already_shared = n
      break 
    else:
      min_cost += can_be_shared * share_cost 
      already_shared += can_be_shared 
  

  min_cost += p*(n-already_shared) 

  
  print(min_cost)



