#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    for (int i=1;i<S.size();i+=4) {
        if (S[i] == 'o') {
            cout << i/4+1 << endl;
            return 0;
        }
    }
    cout << "none" << endl;
}
