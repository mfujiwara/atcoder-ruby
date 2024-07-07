#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,K;
    long long Q;
    cin >> N >> M >> K >> Q;
    vector<long long> A;
    vector<long long> B;
    for (int i=0;i<N;i++) {
        long long p;
        int t;
        cin >> p >> t;
        if (t == 0) {
            A.push_back(p);
        } else {
            B.push_back(p);
        }
    }
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    vector<long long>sumsA(A.size()+1,0);
    vector<long long>sumsB(B.size()+1,0);
    for (int i=0;i<A.size();i++) {
        sumsA[i+1] = sumsA[i]+A[i];
    }
    for (int i=0;i<B.size();i++) {
        sumsB[i+1] = sumsB[i]+B[i];
    }
    long long ret = 1e18;
    for (int i=0;i<=min(M,(int)A.size());i++) {
        if (M-i > B.size()) {
            continue;
        }
        long long sum = sumsA[i]+sumsB[M-i];
        sum += Q*((M-i+K-1)/K);
        ret = min(ret,sum);
    }
    cout << ret << endl;
}
