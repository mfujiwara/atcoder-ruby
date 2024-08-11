#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<pair<int,long long>>> G(N);
    for (int i=0;i<M;i++) {
        int A,B;
        long long C;
        cin >> A >> B >> C;
        A--;B--;
        G[A].push_back({B,C});
        G[B].push_back({A,C});
    }
    bool flag = false;
    long long x = 0;
    vector<long long> memo(N,0);
    vector<long long> group(N,0);
    group[0] = 1;
    set<int> done;
    done.insert(0);
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (auto [u,c]:G[v]) {
            if (done.find(u) != done.end()) {
                if (group[u] != group[v]) {
                    if (memo[u] != c - memo[v]) {
                        cout << -1 << endl;
                        return 0;
                    }
                } else {
                    // memo[u]+memo[v]+group[v]*y*2=c
                    long long y = (c-memo[u]-memo[v])*group[v];
                    if (y%2 != 0) {
                        cout << -1 << endl;
                        return 0;
                    }
                    y /= 2;
                    if (flag) {
                        if (x != y) {
                            cout << -1 << endl;
                            return 0;
                        }
                    } else {
                        x = y;
                        flag = true;
                    }
                }
            } else {
                memo[u] = c - memo[v];
                group[u] = -group[v] ;
                done.insert(u);
                q.push(u);
            }
        }
    }
    if (!flag) {
        x = -1e18;
        for (int i=0;i<N;i++) {
            if (group[i] == 1) {
                x = max(x,-memo[i]);
            }
        }
    }
    for (int i=0;i<N;i++) {
        memo[i] += x*group[i];
        if (memo[i] < 0) {
            cout << -1 << endl;
            return 0;
        }
    }
    for (int i=0;i<N;i++) {
        cout << memo[i] << endl;
    }
}
