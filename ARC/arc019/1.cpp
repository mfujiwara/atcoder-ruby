#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int i=0;i<S.size();i++) {
        if ('0'<=S[i] && S[i]<='9') {
            cout << S[i];
        } else {
            if (S[i]=='O') {
                cout << '0';
            } else if (S[i]=='D') {
                cout << '0';
            } else if (S[i]=='I') {
                cout << '1';
            } else if (S[i]=='Z') {
                cout << '2';
            } else if (S[i]=='S') {
                cout << '5';
            } else if (S[i]=='B') {
                cout << '8';
            }
        }
    }
    cout << endl;
}
