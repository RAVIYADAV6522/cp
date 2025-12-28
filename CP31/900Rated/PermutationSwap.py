t=int(input()) 

for _ in range(t):
  n=int(input())
  arr=list(map(int,input().split(" ")))  

  def GCD(a,b):
    while b!=0:
      a,b=b,a%b 
    return a 

  k=arr[0]-1 
  for i in range(1,len(arr)):
    k=GCD(k,abs(arr[i]-(i+1)))
  print(k)