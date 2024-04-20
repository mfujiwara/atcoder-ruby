#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S,T;
    cin >> S >> T;
    if (S[1]=='F' && T[1]=='F') {
        cout << abs(S[0]-T[0]) << endl;
    } else if (S[0]=='B' && T[0]=='B') {
        cout << abs(S[1]-T[1]) << endl;
    } else if (S[1]=='F' && T[0]=='B') {
        cout << S[0]+T[1]-'0'*2-1 << endl;
    } else {
        cout << S[1]+T[0]-'0'*2-1 << endl;
    }
}
