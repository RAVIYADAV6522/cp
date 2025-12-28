#include <bits/stdc++.h>
using namespace std;

bool check(int n)
{
  while (n > 0)
  {
    if (n % 10 != 7 && n % 10 != 4)
    {
      return false;
    }
    n = n / 10;
  }
  return true;
}

int main()
{
  int n;
  cin >> n;
  bool ans = false;
  for (int i = 1; i <= n; i++)
  {
    if (n % i == 0 && check(i))
    {
      ans = true;
      break;
    }
  }
  if (ans)
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}
