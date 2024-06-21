#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int calc(long long X, string S) {
    long long c=0;
    for (int i=0;i<S.size();i++) {
        if ('0'<=S[i] && S[i]<='9') {
            long long d = c * (S[i]-'0' + 1);
            if (d>=X) {
                X = (X-1)%c+1;
                return calc(X, S);
            }
            c = d;
        } else {
            c+=1;
            if (c==X) {
                cout << S[i] << endl;
                return 0;
            }
        }
    }
}

int main() {
    string S;
    long long X;
    cin >> S >> X;
    calc(X, S);
}
