#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    int v = 0;
    for (int i=0;i<14;i++) {
        if (i%2==0) {
            v += (S[i]-'0')*3;
        } else {
            v += S[i]-'0';
        }
    }
    if (v%10 == S[14]-'0') {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
