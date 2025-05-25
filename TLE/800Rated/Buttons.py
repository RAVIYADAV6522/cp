t=int(input()) 

for _ in range(t):
  a,b,c=map(int,input().split(" ")) 

  if c%2==0:
    AnnaOptions= a+ c//2 
    KatieOptions = b+ c//2
  else:
    AnnaOptions= a+(c//2) +1  
    KatieOptions= b+ c-((c//2) +1  )
  
  if AnnaOptions >KatieOptions:
    print("First") 
  elif AnnaOptions <= KatieOptions:
    print("Second")
