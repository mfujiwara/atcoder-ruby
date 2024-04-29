#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

long long op(long long a, long long b) { return min(a, b); }
long long e() { return (long long)pow(10,15); }

int main() {
    long long N,W,C;
    cin >> N >> W >> C;
    map<long long,long long> memo;
    for (int i=0;i<N;i++) {
        long long l,r,p;
        cin >> l >> r >> p;
        l=max(0ll,l-C+1);
        memo[l]+=p;
        if (r<W-C+1) {
            memo[r]-=p;
        }
    }
    vector<long long> sum;
    sum.push_back(memo[0]);
    for (auto x: memo) {
        if (x.first!=0) {
            sum.push_back(sum.back()+x.second);
        }
    }
    sum.push_back(sum.back()+memo[W-C+1]);
    segtree<long long,op,e> seg(sum);
    long long ret = seg.all_prod();
    cout << ret << endl;
}
