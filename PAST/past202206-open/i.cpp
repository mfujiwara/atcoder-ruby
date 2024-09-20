#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W;
    cin >> H >> W;
    vector<string> S(H);
    pair<int,int> start = make_pair(0,0);
    pair<int,int> aaa = make_pair(0,0);
    pair<int,int> goal = make_pair(0,0);
    for (int i=0;i<H;i++) {
        cin >> S[i];
        for (int j=0;j<W;j++) {
            if (S[i][j] == 's') {
                start.first = i;
                start.second = j;
                S[i][j] = '.';
            } else if (S[i][j] == 'a') {
                aaa.first = i;
                aaa.second = j;
                S[i][j] = '.';
            } else if (S[i][j] == 'g') {
                goal.first = i;
                goal.second = j;
                S[i][j] = '.';
            }
        }
    }
    tuple<int,int,int,int> now = make_tuple(start.first,start.second,aaa.first,aaa.second);
    set<tuple<int,int,int,int>> visited;
    vector<tuple<int,int,int,int>> targets;
    targets.push_back(now);
    int c = 0;
    while (targets.size() > 0) {
        vector<tuple<int,int,int,int>> next_targets;
        for (auto target : targets) {
            int x = get<0>(target);
            int y = get<1>(target);
            int a = get<2>(target);
            int b = get<3>(target);
            if (a == goal.first && b == goal.second) {
                cout << c << endl;
                return 0;
            }
            if (visited.find(target) != visited.end()) {
                continue;
            }
            visited.insert(target);
            if (x > 0 && S[x-1][y] != '#') {
                if (a == x-1 && b == y) {
                    if (a>0 && S[a-1][b] != '#') {
                        next_targets.push_back(make_tuple(x-1,y,a-1,b));
                    }
                } else {
                    next_targets.push_back(make_tuple(x-1,y,a,b));
                }
            }
            if (x < H-1 && S[x+1][y] != '#') {
                if (a == x+1 && b == y) {
                    if (a<H-1 && S[a+1][b] != '#') {
                        next_targets.push_back(make_tuple(x+1,y,a+1,b));
                    }
                } else {
                    next_targets.push_back(make_tuple(x+1,y,a,b));
                }
            }
            if (y > 0 && S[x][y-1] != '#') {
                if (a == x && b == y-1) {
                    if (b>0 && S[a][b-1] != '#') {
                        next_targets.push_back(make_tuple(x,y-1,a,b-1));
                    }
                } else {
                    next_targets.push_back(make_tuple(x,y-1,a,b));
                }
            }
            if (y < W-1 && S[x][y+1] != '#') {
                if (a == x && b == y+1) {
                    if (b<W-1 && S[a][b+1] != '#') {
                        next_targets.push_back(make_tuple(x,y+1,a,b+1));
                    }
                } else {
                    next_targets.push_back(make_tuple(x,y+1,a,b));
                }
            }
        }
        targets = next_targets;
        c++;
    }
    cout << -1 << endl;
}
