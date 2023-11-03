#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int c0=0,c1=0;
    for (int i=0;i<S.size();i++) {
        if (i%2==0) {
            if (S[i]=='0') {
                c1++;
            } else {
                c0++;
            }
        } else {
            if (S[i]=='0') {
                c0++;
            } else {
                c1++;
            }
        }
    }
    cout << min(c0,c1) << endl;
}
