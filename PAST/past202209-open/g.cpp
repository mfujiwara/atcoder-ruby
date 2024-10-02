#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,L,K;
    cin >> N >> L >> K;
    vector<string> S(N);
    for (int i=0;i<N;i++) {
        cin >> S[i];
    }
    int ret = 1;
    for (int bit=0;bit<(1<<L);bit++) {
        vector<int> cut;
        for (int i=0;i<L;i++) {
            if (bit & (1<<i)) {
                cut.push_back(i);
            }
        }
        if (cut.size() != K) {
            continue;
        }
        map<string,int> cnt;
        for (string s : S) {
            string t = "" + s;
            for (int c : cut) {
                t[c] = '_';
            }
            cnt[t]++;
            ret = max(ret, cnt[t]);
        }
    }
    cout << ret << endl;
}
