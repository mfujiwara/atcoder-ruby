#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int X,Y;
    cin >> X >> Y;
    X--;
    Y--;
    vector<pair<int,int>> moves;
    string S;
    for (int i=0;i<3;i++) {
        cin >> S;
        for (int j=0;j<3;j++) {
            if (S[j]=='#') {
                moves.push_back({i-1,j-1});
            }
        }
    }
    vector<vector<bool>> visited(9,vector<bool>(9,false));
    queue<pair<int,int>> q;
    q.push({X,Y});
    visited[X][Y] = true;
    int ret = 1;
    while (!q.empty()) {
        auto [x,y] = q.front();
        q.pop();
        for (auto [dx,dy]:moves) {
            int nx = x+dx;
            int ny = y+dy;
            if (nx<0 || nx>=9 || ny<0 || ny>=9) continue;
            if (visited[nx][ny]) continue;
            visited[nx][ny] = true;
            q.push({nx,ny});
            ret++;
        }
    }
    cout << ret << endl;
}
