t=int(input()) 

for _ in range(t):
  n=int(input()) 
  a=list(map(int,input().split(" "))) 
  
  def helper():
      max_ele=max(a)  
      b=[] 
      c=[] 
      for i in a:
        if i ==max_ele:
          c.append(i) 
        else:
          b.append(i) 
  
      if len(b)==0:
        print(-1) 
        return 
      
      print(len(b), len(c))
      for ele in b:
        print(ele,end=" ")
      print()
      for ele in c:
        print(ele,end=" ")
      print()
  helper()
