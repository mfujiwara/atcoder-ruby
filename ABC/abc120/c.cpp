#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    vector<int> memo(1,-1);
    for (int i;i<S.size();i++) {
        if (S[i] == '0') {
            if (memo[memo.size()-1] == 1) {
                memo.pop_back();
            } else {
                memo.push_back(0);
            }
        } else {
            if (memo[memo.size()-1] == 0) {
                memo.pop_back();
            } else {
                memo.push_back(1);
            }
        }
    }
    cout << S.size() - memo.size() + 1 << endl;
}
