#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long N;
    int M;
    cin >> N >> M;
    set<long long> s;
    s.insert(1);
    s.insert(N);
    vector<tuple<long long,long long,long long>> edges;
    for (int i=0;i<M;i++) {
        long long a,b,c;
        cin >> a >> b >> c;
        s.insert(a);
        s.insert(b);
        edges.push_back(make_tuple(a,b,c));
    }
    int n = s.size();
    mcf_graph<int,long long> g(n);
    map<long long,int> mp;
    int idx = 0;
    long long pre_x = -1;
    for (auto x : s) {
        mp[x] = idx;
        idx++;
        if (pre_x != -1) {
            g.add_edge(mp[pre_x],mp[x],1,x-pre_x);
            g.add_edge(mp[x],mp[pre_x],1,x-pre_x);
        }
        pre_x = x;
    }
    for (int i=0;i<M;i++) {
        long long a,b,c;
        tie(a,b,c) = edges[i];
        g.add_edge(mp[a],mp[b],1,c);
        g.add_edge(mp[b],mp[a],1,c);
    }
    cout << g.flow(0,n-1,1).second << endl;
}
