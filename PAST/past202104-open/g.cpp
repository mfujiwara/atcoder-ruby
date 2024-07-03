#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,Q;
    cin >> N >> M >> Q;
    vector<vector<pair<int,long long>>> G(N);
    for (int i=0;i<M;i++) {
        int a,b;
        long long c;
        cin >> a >> b >> c;
        a--;b--;
        G[a].push_back({b,c});
        G[b].push_back({a,c});
    }
    set<int> done = {0};
    priority_queue<pair<long long,int>> queue;
    for (auto [b,c]:G[0]) {
        queue.push({-c,b});
    }
    for (int i=0;i<Q;i++) {
        int x;
        cin >> x;
        vector<pair<long long, int>> memo;
        while (queue.size() > 0 && queue.top().first >= -x) {
            auto [c,b] = queue.top();
            queue.pop();
            if (done.find(b) != done.end()) {
                continue;
            }
            done.insert(b);
            for (auto [bb,cc]:G[b]) {
                memo.push_back({-cc,bb});
            }
        }
        for (auto [c,b]:memo) {
            queue.push({c,b});
        }
        cout << done.size() << endl;
    }
}
