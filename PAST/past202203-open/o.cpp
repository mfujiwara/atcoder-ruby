#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<int>> G(N);
    for (int i=0;i<M;i++) {
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    dsu uf(N);
    for (int i=0;i<N;i++) {
        if (G[i].size()<=1) continue;
        for (int j=1;j<G[i].size();j++) {
            uf.merge(G[i][0], G[i][j]);
        }
    }
    vector<int> cnt(N);
    for (int i=0;i<N;i++) {
        cnt[uf.leader(i)]++;
    }
    vector<pair<int,int>> counts;
    set<int> done;
    for (int i=0;i<N;i++) {
        if (G[i].size()==0) {
            counts.push_back({1,0});
            continue;
        }
        int l = uf.leader(i);
        if (done.count(l)) continue;
        int r = uf.leader(G[i][0]);
        if (l!=r) {
            counts.push_back({cnt[l],cnt[r]});
        }
        done.insert(l);
        done.insert(r);
    }
    vector<vector<bool>> dp(N,vector<bool>(N,false));
    dp[0][0] = true;
    int x = (N + 2) / 3;
    int y = (N + 1) / 3;
    for (auto [a,b]:counts) {
        for (int i=x;i>=0;i--) {
            for (int j=y;j>=0;j--) {
                if (dp[i][j]) {
                    dp[i+a][j+b] = true;
                    dp[i+b][j+a] = true;
                }
            }
        }
    }
    if (dp[x][y]) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
