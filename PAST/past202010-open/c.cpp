#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    string s;
    vector<vector<int>> rets = vector<vector<int>>(N,vector<int>(M,0));
    for (int i=0;i<N;i++) {
        cin >> s;
        for (int j=0;j<M;j++) {
            if (s[j]=='#') {
                for (int x=-1;x<2;x++) {
                    for (int y=-1;y<2;y++) {
                        if (i+x>=0 && i+x<N && j+y>=0 && j+y<M) {
                            rets[i+x][j+y]++;
                        }
                    }
                }
            }
        }
    }
    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            cout << rets[i][j];
        }
        cout << endl;
    }
}
