#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;
    int ret=0;
    for (int i=0;i<S.size();i++) {
        if (S[i]=='A' && S[i+1]=='B' && S[i+2]=='C') {
            ret++;
        }
    }
    cout << ret << endl;
}
