#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,X,Y;
    cin >> N >> X >> Y;
    set<pair<int, int>> blocks = {};
    for (int i;i<N;i++) {
        int x,y;
        cin >> x >> y;
        blocks.insert(make_pair(x,y));
    }
    int ret = 0;
    blocks.insert(make_pair(0,0));
    vector<pair<int, int>> targets = {{0,0}};
    while (targets.size() > 0) {
        vector<pair<int, int>> new_targets = {};
        for (auto target : targets) {
            int x = target.first;
            int y = target.second;
            if (x == X && y == Y) {
                cout << ret << endl;
                return 0;
            }
            for (int dx=-1;dx<=1;dx++) {
                for (int dy=-1;dy<=1;dy++) {
                    if (dx == 0 && dy == 0) {
                        continue;
                    }
                    if (abs(dx) + abs(dy) == 2 && dy < 0) {
                        continue;
                    }
                    if (abs(x+dx) > 201 || abs(y+dy) > 201) {
                        continue;
                    }
                    if (blocks.find(make_pair(x+dx,y+dy)) == blocks.end()) {
                        new_targets.push_back(make_pair(x+dx,y+dy));
                        blocks.insert(make_pair(x+dx,y+dy));
                    }
                }
            }
        }
        targets = new_targets;
        ret++;
    }
    cout << -1 << endl;
}
