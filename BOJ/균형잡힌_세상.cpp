#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (1) {
    string a;
    getline(cin, a);
    if (a ==) {
      break;
    }
    stack<char> s;
    bool isValid = true;
    for (auto c : a) {
      if (c == '(' || c == '[') {
        s.push(c);
      } else if (c == ')') {
        if (s.empty() || s.top() != '(') {
          isValid = false;
          break;
        }
        s.pop();
      } else if (c == ']') {
        if (s.empty() || s.top() != '[') {
          isValid = false;
          break;
        }
        s.pop();
      }
    }
    if (not s.empty()) {
      isValid = false;
    }
    if (isValid) {
      cout << "yes" << endl;
    } else {
      cout << "no" << endl;
    }
  }
}