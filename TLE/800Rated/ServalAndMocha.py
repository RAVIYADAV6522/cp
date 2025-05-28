t=int(input())

for _ in range(t):
  n=int(input()) 
  arr=list(map(int,input().split(" "))) 

  def GCD(a,b):
    while b!=0:
      a,b=b,a%b 
    return a  
  
  def helper(arr):
    
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        if GCD(arr[i],arr[j]):
          return "yes" 
    return "No" 
  

  print(helper(arr))
      













##  C++ code below --------------------  above python code gives TLE ----------------------------

# #include <iostream>
# #include <vector>
# using namespace std;

# // Function to compute GCD using Euclidean algorithm
# int GCD(int a, int b) {
#     while (b != 0) {
#         int temp = b;
#         b = a % b;
#         a = temp;
#     }
#     return a;
# }

# // Helper function to check if any pair has GCD <= 2
# string helper(const vector<int>& arr) {
#     int n = arr.size();
#     for (int i = 0; i < n; i++) {
#         for (int j = i + 1; j < n; j++) {
#             if (GCD(arr[i], arr[j]) <= 2) {
#                 return "yes";
#             }
#         }
#     }
#     return "No";
# }

# int main() {
#     int t;
#     cin >> t;

#     while (t--) {
#         int n;
#         cin >> n;

#         vector<int> arr(n);
#         for (int i = 0; i < n; i++) {
#             cin >> arr[i];
#         }

#         cout << helper(arr) << endl;
#     }

#     return 0;
# }

    


