#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    vector<string> stack;
    stack.push_back("");
    for (int i=0;i<S.size();i++) {
        if (S[i] == '(') {
            stack.push_back("");
        } else if (S[i] == ')') {
            string tmp = stack.back();
            string tmp2 = stack.back();
            reverse(tmp2.begin(), tmp2.end());
            stack.pop_back();
            stack.back() += tmp + tmp2;
        } else {
            stack.back() += S[i];
        }
    }
    cout << stack[0] << endl;
}
