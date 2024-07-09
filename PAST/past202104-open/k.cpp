#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    map<long long, long long> dp;
    dp[0] = 0;
    long long ret = 0;
    for (int i=0;i<N;i++) {
        long long p,u;
        cin >> p >> u;
        map <long long, long long> nexts;
        for (auto x: dp) {
            if (nexts.find(x.first) == nexts.end()) {
                nexts[x.first] = x.second;
            } else {
                nexts[x.first] = max(nexts[x.first], x.second);
            }
            long long s = x.second + u - p + (x.first + p)/100*20;
            long long r = (x.first + p)%100;
            // key が存在しない場合は追加
            if (nexts.find(r) == nexts.end()) {
                nexts[r] = s;
            } else {
                nexts[r] = max(nexts[r], s);
            }
            ret = max(ret, s);
        }
        dp = nexts;
    }
    cout << ret << endl;
}
