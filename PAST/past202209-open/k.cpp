#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,M;
    cin >> N >> M;
    set<pair<int,int>> ab;
    for (int i=0;i<M;i++) {
        int a,b;
        cin >> a >> b;
        ab.insert({a,b});
    }
    auto st = ab;
    int Q;
    cin >> Q;
    vector<tuple<int,int,int>> queries;
    for (int i=0;i<Q;i++) {
        int t,x,y;
        cin >> t >> x >> y;
        queries.push_back({t,x,y});
        if (t == 1) {
            st.insert({x,y});
        } else if (t==2) {
            st.erase({x,y});
        }
    }
    dsu d(N);
    set<pair<int,int>> dd;
    for (auto [a,b]: st) {
        d.merge(a-1,b-1);
        dd.insert({a,b});
    }
    vector<string> rets;
    for (int i=Q-1;i>=0;i--) {
        int t,x,y;
        tie(t,x,y) = queries[i];
        if (t == 1) {
            st = ab;
            for (int j=0;j<i;j++) {
                int tj,xj,yj;
                tie(tj,xj,yj) = queries[j];
                if (tj == 1) {
                    st.insert({xj,yj});
                } else if (tj==2) {
                    st.erase({xj,yj});
                }
            }
            d = dsu(N);
            dd = set<pair<int,int>>();
            for (auto [a,b]: st) {
                d.merge(a-1,b-1);
                dd.insert({a,b});
            }
        } else if (t==2) {
            d.merge(x-1,y-1);
            dd.insert({x,y});
        } else {
            if (d.same(x-1,y-1)) {
                rets.push_back("Yes");
            } else {
                rets.push_back("No");
            }
        }
    }
    reverse(rets.begin(),rets.end());
    for (auto ret: rets) {
        cout << ret << endl;
    }
}
