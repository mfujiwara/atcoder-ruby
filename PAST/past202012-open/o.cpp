#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    int L = (int)sqrt(M);
    vector<set<int>> G(N);
    int a,b;
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        a--;
        b--;
        G[a].insert(b);
        G[b].insert(a);
    }
    vector<set<int>> G2(N);
    for (int i = 0; i < N; i++) {
        for (int j : G[i]) {
            if ((int)G[j].size() >= L) {
                G2[i].insert(j);
            }
        }
    }
    int Q;
    cin >> Q;
    vector<int> send(N);
    vector<int> receive(N);
    int t,x;
    for (int i = 0; i < Q; i++) {
        cin >> t >> x;
        x--;
        if (t == 1) {
            if ((int)G[x].size() < L) {
                for (int j : G[x]) {
                    receive[j] += 1;
                }
            } else {
                send[x] += 1;
            }
        } else {
            int plus = 0;
            for (int j : G2[x]) {
                plus += send[j];
            }
            cout << receive[x] + plus << endl;
            receive[x] = -plus;
        }
    }
}
