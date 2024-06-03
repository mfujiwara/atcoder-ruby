#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<string> A(N);
    vector<pair<int,int>> walls;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        for (int j=0;j<M;j++) {
            if (A[i][j] == '#') {
                walls.push_back(make_pair(i,j));
            }
        }
    }
    int ret = 0;
    for (int i=0;i<walls.size();i++) {
        set<pair<int,int>> done;
        int x = walls[i].first;
        int y = walls[i].second;
        done.insert(make_pair(x,y));
        queue<pair<int,int>> q;
        q.push(make_pair(x,y));
        while (!q.empty()) {
            pair<int,int> p = q.front();
            q.pop();
            int x = p.first;
            int y = p.second;
            if (x > 0 && A[x-1][y] == '.' && done.find(make_pair(x-1,y)) == done.end()) {
                done.insert(make_pair(x-1,y));
                q.push(make_pair(x-1,y));
            }
            if (x < N-1 && A[x+1][y] == '.' && done.find(make_pair(x+1,y)) == done.end()) {
                done.insert(make_pair(x+1,y));
                q.push(make_pair(x+1,y));
            }
            if (y > 0 && A[x][y-1] == '.' && done.find(make_pair(x,y-1)) == done.end()) {
                done.insert(make_pair(x,y-1));
                q.push(make_pair(x,y-1));
            }
            if (y < M-1 && A[x][y+1] == '.' && done.find(make_pair(x,y+1)) == done.end()) {
                done.insert(make_pair(x,y+1));
                q.push(make_pair(x,y+1));
            }
        }
        if (done.size()-1 == N*M-walls.size()) {
            ret++;
        }
    }
    cout << ret << endl;
}
