#include <bits/stdc++.h>
using namespace std;

int main() {
    string S,T;
    cin >> S >> T;
    int len = S.length();
    for (int i=0;i<len;i++) {
        if (S == T) {
            cout << "Yes" << endl;
            return 0;
        }
        S = S[len-1] + S.substr(0,len-1);
    }
    cout << "No" << endl;
}
