#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    set<pair<int,int>> s;
    for (int i=0;i<Q;i++) {
        int t,a,b;
        cin >> t >> a >> b;
        a--; b--;
        if (a>b) swap(a,b);
        if (t==1) {
            if (s.count({a,b})) {
                s.erase({a,b});
            } else {
                s.insert({a,b});
            }
        } else {
            dsu uf(N);
            for (auto [x,y]:s) {
                uf.merge(x, y);
            }
            cout << (uf.same(a,b) ? "Yes" : "No") << endl;
        }
    }
}
