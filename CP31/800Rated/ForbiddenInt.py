t=int(input()) 

for _ in range(t):
  n,k,x=map(int,input().split(" ")) 

  def helper(n,k,x):
    ans=[] 
    if x!=1:
      ans=[1]*(n) 
      print("Yes")
      print(len(ans))
      print(*ans)
    
    elif x==1:
      if k==1:
        print("No") 

      elif k==2:
        if n%2==0:
          ans=[2]*(n//2) 
          print("Yes") 
          print(len(ans))
          print(*ans) 
        else:
          print("No") 

      elif k>=3:
        if n%2==0:
          ans=[2]*(n//2) 
          print("Yes") 
          print(len(ans))
          print(*ans)  
        else:
          ans=[2]*((n-3)//2) 
          ans.append(3) 
          print("Yes") 
          print(len(ans))
          print(*ans) 
  helper(n,k,x)        

           
           







