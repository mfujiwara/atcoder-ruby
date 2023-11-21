#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int l = S.size();
    for (int i=0;i<l/2;i++) {
        if (S[i]==S[l-1-i] || S[i]=='*' || S[l-1-i]=='*') {
            continue;
        } else {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}
