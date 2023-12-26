#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int i=0;i<S.size();i++) {
        if (i==0) {
            if (islower(S[i])) {
                S[i] = toupper(S[i]);
            }
        } else {
            if (isupper(S[i])) {
                S[i] = tolower(S[i]);
            }
        }
    }
    cout << S << endl;
}
