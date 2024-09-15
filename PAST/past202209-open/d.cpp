#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    set<pair<int,int>> s;
    for (int i=0;i<M;i++) {
        int u,v;
        cin >> u >> v;
        if (u==v || s.count({u,v}) || s.count({v,u}) || u>N || v>N) {
            cout << "No" << endl;
            return 0;
        }
        s.insert({u,v});
    }
    cout << "Yes" << endl;
}
