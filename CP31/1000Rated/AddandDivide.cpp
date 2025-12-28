#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long a, b;
        cin >> a >> b;
        
        
        long long ans=INT_MAX;
        for(int ops=0;ops<32;ops++){ // consider the case when without any addition ops ( just dividing ) we can get the minimum ans.
           long long Addoperations = ops;
           long long new_b=b + Addoperations;
           if(new_b==1){
            continue; 
           }
           long long new_a=a;
           while(new_a >0){
              new_a=new_a/new_b; 
              Addoperations++;
           }
           ans=min(ans,Addoperations);
           


        }
        cout << ans <<endl;
        
    }
}