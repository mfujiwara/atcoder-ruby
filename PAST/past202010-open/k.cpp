#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long MOD=1000000000;
    int K;
    cin >> K;
    vector<vector<int>> A(K);
    vector<vector<long long>> counts(K, vector<long long>(22,0));
    vector<long long> retCounts(K,0);
    for (int i=0;i<K;i++) {
        int n;
        cin >> n;
        A[i].resize(n);
        for (int j=0;j<n;j++) {
            cin >> A[i][j];
            for (int k=A[i][j]+1;k<21;k++) {
                retCounts[i] += counts[i][k];
                retCounts[i] %= MOD;
            }
            counts[i][A[i][j]]++;
        }
    }
    vector<long long> totalCounts(22,0);
    long long ret = 0;
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int b;
        cin >> b;
        b-=1;
        ret += retCounts[b];
        for (int i=1;i<21;i++) {
            for (int j=i+1;j<21;j++) {
                ret += counts[b][i]*totalCounts[j];
                ret %= MOD;
            }
            totalCounts[i] += counts[b][i];
        }
    }
    cout << ret << endl;
}
