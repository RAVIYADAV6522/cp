t=int(input()) 

for _ in range(t):
  n=int(input()) 
  a=list(map(int,input().split(" "))) 
  ans=[]
  def helper(a):
      
      count=1 
      for i in range(1,len(a)):
        if a[i]==a[i-1]:
          count+=1 
      if count==len(a):
         return ans 
      
      i=0
      j=len(a)-1
      while(i<j):
         ans.append(a[i]) 
         ans.append(a[j]) 
         i+=1
         j-=1 
      if i==j:
         ans.append(a[i]) 
      
      return ans 
  arr=helper(a)
  if len(arr)==0:
     print("NO") 
  else:
     print("Yes") 
     print(*arr)
     
         


