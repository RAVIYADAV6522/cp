#include <bits/stdc++.h>
using namespace std;

int main()
{

  int t;
  cin >> t;
  while (t--)
  {
    int n;
    cin >> n;

    vector<long long> p(n);
    for (int i = 0; i < n; i++)
    {
      cin >> p[i];
    }

    // logic goes hare
    int flag=0;
    for(int i=1;i<n-1;i++){
      if(p[i]>p[i-1] && p[i]>p[i+1]){
        flag=1;
        cout<<"Yes"<<'\n';
        cout<<i<<" "<<i+1<<" "<<i+2<<'\n';
        break;
      }
      
    }
    if(flag==0){
      cout<<"No"<<'\n';
    }
    
  }
  return 0;
} 