#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin>>A[i];
    }
    vector<map<tuple<int,int>, long long>> mps(3);
    for (int i=0;i<M;i++) {
        long long P;
        int Q,L,R;
        cin >> P >> Q >> L >> R;
        int mod = (L+R)%3;
        mps[mod][{Q-1,L}] += P;
    }
    long long ret = 0;
    for (int mod=0;mod<3;mod++) {
        map<int, long long> dp;
        dp[0] = mps[mod][{0,0}];
        for (int i=0;i<N;i++) {
            map<int,long long> nexts;
            for (auto [key, val]: dp) {
                nexts[key] = max(nexts[key], val+mps[mod][{i+1,key}]);
                nexts[(key+1)%3] = max(nexts[(key+1)%3], val+A[i]+mps[mod][{i+1,(key+1)%3}]);
            }
            dp = nexts;
        }
        ret = max(ret, dp[mod]);
    }
    cout << ret << endl;
}
