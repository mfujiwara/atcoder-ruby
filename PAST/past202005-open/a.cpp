#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string s,t;
    cin >> s >> t;
    if (s==t) {
        cout << "same" << endl;
        return 0;
    }
    for (int i=0;i<s.size();i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = s[i] - 'A' + 'a';
        }
    }
    for (int i=0;i<t.size();i++) {
        if (t[i] >= 'A' && t[i] <= 'Z') {
            t[i] = t[i] - 'A' + 'a';
        }
    }
    if (s == t) {
        cout << "case-insensitive" << endl;
    } else {
        cout << "different" << endl;
    }
}
