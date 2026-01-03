t=int(input())

for _ in range(t):
  n=int(input())
  s=input().strip() 

  Total_distinct = 0
  distinct_char = set() 

  ## idea : for length n distinct substring , n-1 length substring is common  
  ## example S = abcad  , 3 length distinct substring = cad , bad , aad  Note : ad substring is common 
  for i in range(n):
    distinct_char.add(s[i]) 
    Total_distinct += len(distinct_char) 
  
  print(Total_distinct) 

  
    
 
