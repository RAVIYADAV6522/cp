# t=int(input()) 

# for _ in range(t):
#   n,s=map(int,(input().split()))
#   arr=list(map(int,input().split()))  

#   mini=min(s-arr[0],arr[-1]-s) 
#   ans=0
#   if s>arr[-1]:
#     ans+=s-arr[0]
#   elif s<arr[0]:
#     ans+=arr[-1]-s
#   elif arr[-1]-s ==0:
#     ans=s-arr[0] 
#   elif s-arr[0]==0:
#     ans+= arr[-1]-s
 
#   else:
#     ans+=2*mini + max(s-arr[0],arr[-1]-s) 
  
#   print(ans)




# t=int(input())

# for _ in range(t):
#     n=int(input())
#     s=input() 

#     def subString(S,b):
#         i=j=0
#         while i<len(S) and j<len(b):
#             if S[i]==b[j]:
#                 i+=1
#                 j+=1 
#             else:
#                 i+=1 
#         return j==len(b) 
    
#     ans=False 
#     for i in range(1,len(s)-1):
#         if subString(s[:i],s[i]) or subString(s[i+1],s[i]):
#             ans=True 
#     if ans:
#         print("Yes") 
#     else:
#         print("No")
        
        
        
        
        



# t=int(input())

# for _ in range(t):
#   l,r=map(int,(input().split())) 

#   def compare(n,x):
#     n=str(n)
#     x=str(x) 
#     count=0
#     for i in range( min( len(n),len(x) ) ):
#       if n[i]==x[i]:
#         count+=1 
#     return count 
   
#   ans=l 
  
    
#   while l<r:
#       m=(l+r)//2
#       calculate=compare(l,m) + compare(m,r)
#       if calculate<ans:
#         ans=calculate  
          
#       r=m  
#   print(ans) 





# t=int(input()) 

# for _ in range(t):
#   s=input() 

#   arr=list(s) 
#   ans=[]
  
    

#   f=t=n=0
#   for ch in s: 
#     if ch =="F":
#       f+=1 
#     elif ch == "T":
#       t+=1 
#     elif ch == "N":
#       n+=1 
#     else:
#       ans.append(ch)
  
#   final=t*"T" + f*"F" + n*"N" + ''.join(ans) 
#   print(final)

  




# t1,t2,t3,t4 = map(float,input().split()) 
# t=float(input()) 

# arr=[t1,t2,t3,t4] 
# arr.sort() 

# x=3*t -(arr[1]+ arr[2]) 

# if x>arr[0] and x<arr[-1]:
#   print(round(x,2)) 
# elif x>=arr[-1]:
#   print("infinite") 
# elif x<arr[0]:
#   print("impossible") 


t=int(input()) 
for _ in range(t):
  k,x = map(int,input().split()) 

  while k>0:
    x=x*2 
    k-=1 
  print(x)
