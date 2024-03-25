#include <bits/stdc++.h>
using namespace std;

int main() {
    long long MOD=1000000007;
    long long N,K;
    cin >> N >> K;
    // Kの約数一覧を求める
    vector<long long> divisors;
    for (long long i = 1; i * i <= K; ++i) {
        if (K % i != 0) continue;
        divisors.push_back(i);
        if (K / i != i) divisors.push_back(K / i);
    }
    sort(divisors.begin(), divisors.end());
    // sums[i] := 1からNまでの数の divisors[i] の倍数の合計
    vector<long long> sums(divisors.size(), 0);
    for (int i=0;i<divisors.size();i++) {
        long long d = divisors[i];
        long long n = N/d;
        sums[i] = (n*(n+1)/2%MOD)%MOD;
    }
    // 係数を求めておく
    vector<long long> factor(divisors.size(),K);
    for (int i=0;i<divisors.size();i++) {
        for (int j=0;j<i;j++) {
            if (divisors[i]%divisors[j]==0) {
                factor[i] -= factor[j]*(divisors[i]/divisors[j])%MOD;
                factor[i] = (factor[i]+MOD)%MOD;
            }
        }
    }
    long long ret = 0;
    for (int i=0;i<divisors.size();i++) {
        ret += sums[i]*factor[i]%MOD;
        ret %= MOD;
    }
    cout << ret << endl;
}
