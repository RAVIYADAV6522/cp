t = int(input().strip())
for _ in range(t):
  n = int(input().strip())
  a = list(map(int, input().split()))

        # Count frequencies
  freq = {} 
  for num in a:
    freq[num] = freq.get(num, 0) + 1  
  
  current_highest_freq = max(freq.values()) 

  ops=0 
  while current_highest_freq < n:
    ## clone 
    ops+=1 

    ## swap conditions -- 
    if current_highest_freq *2 <=n:
      ops+=current_highest_freq 
      current_highest_freq*=2 
    else:
      ops+=(n-current_highest_freq) 
      current_highest_freq=n  
  print(ops)