#include <iostream>
#include <algorithm> // for max and min fx
using namespace std; 

int main() 
{
  int A,B,C;
  cin >>A>>B>>C;
  
  cout << min(A,B,C) << " " << max(A,B,C)<< endl;
  return 0; 
}