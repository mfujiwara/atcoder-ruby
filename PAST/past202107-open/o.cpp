#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<long long> A;
    vector<long long> sums;
    vector<pair<int,long long>> B;
    long long maxB = 0;
    for (int i=0;i<N;i++) {
        long long a,b;
        cin >> a >> b;        
        A.push_back(a);
        if (i==0) {
            sums.push_back(a);
        } else {
            sums.push_back(sums[i-1]+a);
        }
        if (maxB < b) {
            maxB = b;
            B.push_back(make_pair(i,b));
        }
    }
    sums.push_back(sums[N-1]);
    B.push_back(make_pair(N,1e18));
    vector<long long> memo = vector<long long>(N+1,-1);
    memo[0] = A[0];
    int b_index = 0;
    for (int i=0;i<N;i++) {
        auto c = memo[i];
        if (c==-1) {
            continue;
        }
        while (B[b_index].second <= c) {
            memo[B[b_index+1].first] = c-B[b_index].second+sums[B[b_index+1].first]-sums[i];
            b_index++;
        }
    }
    cout << memo[N] << endl;
}
