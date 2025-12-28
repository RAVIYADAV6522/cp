t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
   

    prev=0
    prefix_sum=[0]*(len(arr)) 
    for i in range(n):
        prefix_sum[i]=arr[i]+prev  
        prev+=arr[i]  
    
   
    for i in range(q):
        l, r, k = map(int, input().split()) 

        new_Sum = prefix_sum[-1] - (prefix_sum[r-1]- ( prefix_sum[l-2] if l>1 else 0 )) + (r-l+1)*k  

        if new_Sum%2==1:
            print("Yes") 
        else:
            print("NO") 


        
        
