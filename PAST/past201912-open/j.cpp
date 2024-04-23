#include <bits/stdc++.h>
#include <atcoder/all>
#include <queue>
using namespace std;
using namespace atcoder;

vector<vector<int>> calc(int H,int W,vector<vector<int>> A,int h,int w) {
    vector<vector<int>> ret(H, vector<int>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            ret[i][j] = (int)pow(10,10);
        }
    }
    ret[h][w] = 0;
    priority_queue<vector<int>> que;
    que.push({0,h,w});
    while (!que.empty()) {
        int cost = -que.top()[0];
        int x = que.top()[1];
        int y = que.top()[2];
        que.pop();
        if (x>0) {
            if (ret[x-1][y] > cost+A[x-1][y]) {
                ret[x-1][y] = cost+A[x-1][y];
                que.push({-(cost+A[x-1][y]),x-1,y});
            }
        }
        if (x<H-1) {
            if (ret[x+1][y] > cost+A[x+1][y]) {
                ret[x+1][y] = cost+A[x+1][y];
                que.push({-(cost+A[x+1][y]),x+1,y});
            }
        }
        if (y>0) {
            if (ret[x][y-1] > cost+A[x][y-1]) {
                ret[x][y-1] = cost+A[x][y-1];
                que.push({-(cost+A[x][y-1]),x,y-1});
            }
        }
        if (y<W-1) {
            if (ret[x][y+1] > cost+A[x][y+1]) {
                ret[x][y+1] = cost+A[x][y+1];
                que.push({-(cost+A[x][y+1]),x,y+1});
            }
        }
    }
    return ret;
}

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<int>> A(H, vector<int>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> A[i][j];
        }
    }
    int ret = (int)pow(10,10);
    vector<vector<int>> p1 = calc(H,W,A,0,W-1);
    vector<vector<int>> p2 = calc(H,W,A,H-1,0);
    vector<vector<int>> p3 = calc(H,W,A,H-1,W-1);
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            ret = min(ret,p1[i][j]+p2[i][j]+p3[i][j]-2*A[i][j]);
        }
    }
    cout << ret << endl;
}
