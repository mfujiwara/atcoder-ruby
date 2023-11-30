#include <bits/stdc++.h>
using namespace std;

int main() {
    string X,s;
    cin >> X >> s;
    string ret = "";
    for (int i=0;i<s.size();i++) {
        if (s[i] != X[0]) {
            ret += s[i];
        }
    }
    cout << ret << endl;
}
