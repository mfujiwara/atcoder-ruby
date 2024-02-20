#include <bits/stdc++.h>
using namespace std;

int main() {
    long long MOD = 1000000007;
    int N;
    cin >> N;
    long long ret = 1;
    for (int i=1;i<=N;i++) {
        ret = (ret * i) % MOD;
    }
    cout << ret << endl;
}
