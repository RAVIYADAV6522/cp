t=int(input()) 
for _ in range(t):
    n,k=map(int,input().split(" ")) 
    arr=list(map(int,input().split(" ")))

    copy = arr[:] 

    if sorted(copy)==arr:
      print("YES")    
    elif k==1:
      print("NO") 
    else:
      print("YES") 




