#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    int sx,sy,gx,gy;
    vector<vector<pair<int,int>>> memo(10,vector<pair<int,int>>(0));
    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            char c;
            cin >> c;
            if (c == 'S') {
                sx = i;
                sy = j;
            } else if (c == 'G') {
                memo[9].push_back(make_pair(i,j));
            } else {
                memo[c-'1'].push_back(make_pair(i,j));
            }
        }
    }
    vector<vector<int>> now = {{sx,sy,0}};
    for (int i=0;i<10;i++) {
        vector<vector<int>> next;
        for (int j=0;j<memo[i].size();j++) {
            int x = memo[i][j].first;
            int y = memo[i][j].second;
            int c = 1000000000;
            for (int k=0;k<now.size();k++) {
                int nx = now[k][0];
                int ny = now[k][1];
                int n = now[k][2];
                int d = abs(x-nx) + abs(y-ny) + n;
                if (d < c) {
                    c = d;
                }
            }
            next.push_back({x,y,c});
        }
        now = next;
        if (now.size() == 0) {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << now[0][2] << endl;
}
