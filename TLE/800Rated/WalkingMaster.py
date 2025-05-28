t=int(input()) 

for _ in range(t):
  a,b,c,d=map(int,input().split(" "))  

  def helper(a,b,c,d):
    if d<b:
      return -1 
    elif d>=b:
      movesY=d-(b) 
      b+=movesY
      movesX=movesY 
      a+=movesX

      # // y has achieved check for x ( achived or not)
      if b==d:
        if a<c:
          return -1 
        else:
          ans=(a-(c)) + movesY 
          return ans  
  print(helper(a,b,c,d))


    

