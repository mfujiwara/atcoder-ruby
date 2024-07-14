#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    if ((S.size()>1 && S[0]=='0') || S.size() > 10) {
        cout << "No" << endl;
        return 0;
    }
    long long N = stoll(S);
    long long L,R;
    cin >> L >> R;
    if (N < L || N > R) {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
}
