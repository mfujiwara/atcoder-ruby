#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    int oc=0;
    int xc=0;
    for (int i=0;i<5;i++) {
        if (S[i]=='o') {
            xc=0;
            oc++;
            if (oc==3) {
                cout << "o" << endl;
                return 0;
            }
        } else {
            oc=0;
            xc++;
            if (xc==3) {
                cout << "x" << endl;
                return 0;
            }
        }
    }
    cout << "draw" << endl;
}
