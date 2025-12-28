#include <iostream>
using namespace std;

int main()
{
  long long N, M;
  cin >> N >> M;
  int lastN = N%10;
  int lastM = M%10;
  cout << lastN + lastM<<endl;

  return 0;
}