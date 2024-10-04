#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string S;
    cin >> S;
    int c = 0;
    for (int i=0;i<S.size();i++) {
        if (S[i] == '(') {
            c++;
        } else {
            c--;
            if (c < 0) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    if (c == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
