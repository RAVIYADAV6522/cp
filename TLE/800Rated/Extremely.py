t=int(input()) 

def checkRoundNumber(n):
  countZeros=0
  countDigits=0
  while(n>0):
    if n%10==0:
      countZeros+=1 
    n=n//10 
    countDigits+=1 
  return countZeros==countDigits-1 

def allRoundNumbers():
      arr=[]
      for i in range(1,999999):
        if checkRoundNumber(i):
          arr.append(i) 
      return arr


for _ in range(t):
  n=int(input())

  def helper(n):
      a=allRoundNumbers()
      ans=0
      for i in range(len(a)):
          if a[i]<=n:
            ans+=1
          else:
             break 
      return ans  

  print(helper(n))
  
  

  

 