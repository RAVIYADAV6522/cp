#include <bits/stdc++.h>
using namespace std;

int main()
{
  

  int t;
  cin >> t;
  while (t--)
  {
    int n,r,b;
    cin >> n >> r >>b;
   
    string s;
    int len_of_red = r/(b+1);
    int extra_red = r%(b+1);

    for(int i=1;i<=b+1;i++){
        for(int j=1;j<=len_of_red;j++){
            s+="R";
        }
        if(extra_red>0){
            s+="R";
            extra_red--;
        }
        if(i!=b+1){
            s+="B";
        }
    }
    cout<<s<<'\n';
    

  }
  return 0;

}