#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,Q;
    cin >> N >> Q;
    // N*Nの2次元配列
    vector<vector<bool>> G(N, vector<bool>(N, false));
    for (int i=0;i<Q;i++) {
        int q;
        cin >> q;
        if (q == 1) {
            int a,b;
            cin >> a >> b;
            a--; b--;
            G[a][b] = true;
        } else if (q == 2) {
            int a;
            cin >> a;
            a--;
            for (int j=0;j<N;j++) {
                if (G[j][a]) {
                    G[a][j] = true;
                }
            }
        } else {
            int a;
            cin >> a;
            a--;
            vector<int> friends;
            for (int j=0;j<N;j++) {
                if (G[a][j]) {
                    friends.push_back(j);
                }
            }
            for (int j=0;j<friends.size();j++) {
                for (int k=0;k<N;k++) {
                    if (G[friends[j]][k] && a != k) {
                        G[a][k] = true;
                    }
                }
            }
        }
    }
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            cout << (G[i][j] ? "Y" : "N");
        }
        cout << endl;
    }
}
