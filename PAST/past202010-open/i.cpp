#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<long long> A(2*N);
    long long total = 0;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        A[i+N] = A[i];
        total += A[i];
    }
    vector<long long> sum(2*N+1);
    for (int i=0;i<2*N;i++) {
        sum[i+1] = sum[i] + A[i];
    }
    long long ret = 1000000000000000000;
    for (int i=0;i<N;i++) {
        long long target = total/2 + sum[i];
        int idx = lower_bound(sum.begin(),sum.end(),target)-sum.begin();
        ret = min(ret,abs(total-(sum[idx]-sum[i])*2));
        ret = min(ret,abs(total-(sum[idx+1]-sum[i])*2));
    }
    cout << ret << endl;
}
