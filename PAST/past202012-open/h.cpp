#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int H,W,r,c;
    cin >> H >> W >> r >> c;
    r--;c--;
    vector<string> S(H);
    vector<vector<string>> rets(H, vector<string>(W, "x"));
    for (int i=0;i<H;i++) {
        cin>>S[i];
        for (int j=0;j<W;j++) {
            if (S[i][j] == '#') {
                rets[i][j] = "#";
            }
        }
    }
    rets[r][c] = "o";
    vector<pair<int,int>> targets = {{r,c}};
    while (targets.size() > 0) {
        vector<pair<int,int>> new_targets;
        for (auto target: targets) {
            int x = target.first;
            int y = target.second;
            if (x > 0 && rets[x-1][y] == "x" && (S[x-1][y] == '.' || S[x-1][y] == 'v')) {
                rets[x-1][y] = "o";
                new_targets.push_back({x-1,y});
            }
            if (x < H-1 && rets[x+1][y] == "x" && (S[x+1][y] == '.' || S[x+1][y] == '^')) {
                rets[x+1][y] = "o";
                new_targets.push_back({x+1,y});
            }
            if (y > 0 && rets[x][y-1] == "x" && (S[x][y-1] == '.' || S[x][y-1] == '>')) {
                rets[x][y-1] = "o";
                new_targets.push_back({x,y-1});
            }
            if (y < W-1 && rets[x][y+1] == "x" && (S[x][y+1] == '.' || S[x][y+1] == '<')) {
                rets[x][y+1] = "o";
                new_targets.push_back({x,y+1});
            }
        }
        targets = new_targets;
    }
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cout << rets[i][j];
        }
        cout << endl;
    }
}
