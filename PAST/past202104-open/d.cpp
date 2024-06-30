#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,K;
    cin >> N >> K;
    vector<long long> sums(N+1,0);
    for (int i=0;i<N;i++) {
        long long A;
        cin >> A;
        sums[i+1] = sums[i]+A;
    }
    for (int i=0;i<=N-K;i++) {
        cout << sums[i+K]-sums[i] << endl;
    }
}
