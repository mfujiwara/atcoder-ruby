#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

vector<pair<int,int>> calc(vector<vector<int>> S, int x, int y, int c) {
    if (c==1) {
        return {{x,y}};
    }
    int H = S.size();
    int W = S[0].size();
    S[x][y] = 0;
    if (x+1<H && S[x+1][y]==1) {
        auto res = calc(S, x+1, y, c-1);
        if (res.size()>0) {
            res.push_back({x,y});
            return res;
        }
    }
    if (y+1<W && S[x][y+1]==1) {
        auto res = calc(S, x, y+1, c-1);
        if (res.size()>0) {
            res.push_back({x,y});
            return res;
        }
    }
    if (x-1>=0 && S[x-1][y]==1) {
        auto res = calc(S, x-1, y, c-1);
        if (res.size()>0) {
            res.push_back({x,y});
            return res;
        }
    }
    if (y-1>=0 && S[x][y-1]==1) {
        auto res = calc(S, x, y-1, c-1);
        if (res.size()>0) {
            res.push_back({x,y});
            return res;
        }
    }
    S[x][y] = 1;
    return {};
}

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<int>> S(H, vector<int>(W,0));
    int c = 0;
    for (int i=0;i<H;i++) {
        string s;
        cin >> s;
        for (int j=0;j<W;j++) {
            if (s[j]=='#') {
                S[i][j] = 1;
                c++;
            }
        }
    }
    cout << c << endl;
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (S[i][j]==1) {
                auto res = calc(S, i, j, c);
                if (res.size()>0) {
                    for (auto p: res) {
                        cout << p.first+1 << " " << p.second+1 << endl;
                    }
                    return 0;
                }
            }
        }
    }
}
