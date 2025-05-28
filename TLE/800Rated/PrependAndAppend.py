t=int(input()) 

for _ in range(t):
  n=int(input()) 
  s=input() 
  
  def helper(s):
      if len(s)==0 or len(s)==1:
        return len(s) 
      
      i=0
      j=len(s)-1 
      while(i<=j):
        if s[i]!=s[j]:
          i+=1
          j-=1 
        else:
          return j-i+1
      return 0  
  print(helper(s))