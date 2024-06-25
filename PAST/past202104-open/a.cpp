#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    bool flag = true;
    for (int i=0;i<S.size();i++) {
        if (i==3) {
            if (S[i]!='-') {
                flag = false;
                break;
            }
        } else {
            if (S[i]<'0' || S[i]>'9') {
                flag = false;
                break;
            }
        }
    }
    if (flag) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
