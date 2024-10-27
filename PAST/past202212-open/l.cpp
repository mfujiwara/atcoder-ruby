#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<pair<long long, long long>> LR;
    for (int i=0;i<N;i++) {
        long long L,R;
        cin >> L >> R;
        LR.push_back(make_pair(L,-R));
    }
    sort(LR.begin(), LR.end());
    vector<long long> memo;
    for (int i=0;i<N;i++) {
        long long r = LR[i].second;
        auto it = lower_bound(memo.begin(), memo.end(), r+1);
        if (it == memo.end()) {
            memo.push_back(r);
        } else {
            *it = r;
        }
    }
    cout << memo.size() << endl;
}
