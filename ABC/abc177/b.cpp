#include <bits/stdc++.h>
using namespace std;

int main() {
    string S,T;
    cin >> S >> T;
    int n = S.size();
    int m = T.size();
    int ret = 1000;
    for (int i=0;i<=n-m;i++) {
        int cnt = 0;
        for (int j=0;j<m;j++) {
            if (S[i+j] != T[j]) {
                cnt++;
            }
        }
        ret = min(ret, cnt);
    }
    cout << ret << endl;
}
