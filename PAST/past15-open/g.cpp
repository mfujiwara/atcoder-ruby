#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<pair<int,int>>> memo(M);
    for (int i=0;i<M;i++) {
        int k;
        cin >> k;
        for (int j=0;j<k;j++) {
            int a,b;
            cin >> a >> b;
            a--;
            memo[i].push_back({a,b});
        }
    }
    for (long long bit=0;bit<(1<<N);bit++) {
        bool okok = true;
        for (int i=0;i<M;i++) {
            bool ok = false;
            for (auto [a,b]:memo[i]) {
                if (((bit>>a)&1) == b) {
                    ok = true;
                    break;
                }
            }
            if (!ok) {
                okok = false;
                break;
            }
        }
        if (okok) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
