#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long N,K;
    cin >> N >> K;
    vector<long long> A(N);
    long long sum = 0;
    for (int i=0;i<N;i++) {
        cin>>A[i];
        sum += A[i];
    }
    long long ret;
    if (K==1) {
        ret = sum;
    } else {
        // N-1 C K-1
        ret = 1;
        for (int i=0;i<K-1;i++) {
            ret *= N-1-i;
            ret /= i+1;
        }
        ret *= sum;
    }
    cout << ret << endl;
}
