#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int D;
    cin >> D;
    string N;
    cin >> N;
    vector<long long> cnt(10);
    for (char c : N) {
        cnt[c - '0']++;
    }
    long long ans = 0;
    for (long long i=0;i<9;i++) {
        for (long long j=i+1;j<10;j++) {
            ans += (j - i) * cnt[i] * cnt[j];
        }
    }
    cout << ans << endl;
}
