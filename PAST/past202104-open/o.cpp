#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

template<typename T=int> // T: type of cost
struct lca {
  int n, root, l;
  vector<vector<int>> to;
  vector<vector<T>> co;
  vector<int> dep;
  vector<T> costs;
  vector<vector<int>> par;
  lca(int n):n(n),to(n),co(n),dep(n),costs(n) {
    l = 0;
    while ((1<<l) < n) ++l;
    par = vector<vector<int>>(n+1,vector<int>(l,n));
  }
  void addEdge(int a, int b, T c=1) {
    to[a].push_back(b); co[a].push_back(c);
    to[b].push_back(a); co[b].push_back(c);
  }
  void dfs(int v, int d=0, T c=0, int p=-1) {
    if (p != -1) par[v][0] = p;
    dep[v] = d;
    costs[v] = c;
    for (int i = 0; i < to[v].size(); ++i) {
      int u = to[v][i];
      if (u == p) continue;
      dfs(u, d+1, c+co[v][i], v);
    }
  }

  void init(int _root=0) {
    root = _root;
    dfs(root);
    for (int i = 0; i < l-1; ++i) {
      for (int v = 0; v < n; ++v) {
        par[v][i+1] = par[par[v][i]][i];
      }
    }
  }
  // LCA
  int up(int v, int k) {
    for (int i = l-1; i >= 0; --i) {
      int len = 1<<i;
      if (k >= len) k -= len, v = par[v][i];
    }
    return v;
  }
  int operator()(int a, int b) {
    if (dep[a] > dep[b]) swap(a,b);
    b = up(b, dep[b]-dep[a]);
    if (a == b) return a;
    for (int i = l-1; i >= 0; --i) {
      int na = par[a][i], nb = par[b][i];
      if (na != nb) a = na, b = nb;
    }
    return par[a][0];
  }
  int length(int a, int b) {
    int c = (*this)(a,b);
    return dep[a]+dep[b]-dep[c]*2;
  }
  T dist(int a, int b) {
    int c = (*this)(a,b);
    return costs[a]+costs[b]-costs[c]*2;
  }
};

vector<int> dist(int a, int N, vector<vector<int>> g) {
    vector<int> ret = vector<int>(N,-1);
    vector<int> targets = {a};
    ret[a] = 0;
    int c = 1;
    while (targets.size() > 0) {
        vector<int> next_targets;
        for (auto t:targets) {
            for (auto u:g[t]) {
                if (ret[u] != -1) {
                    continue;
                }
                ret[u] = c;
                next_targets.push_back(u);
            }
        }
        targets = next_targets;
        c++;
    }
    return ret;
};

int main() {
    int N,M;
    cin >> N >> M;
    lca<int> lca(N);
    vector<vector<int>> all_graph(N,vector<int>());
    set<int> s;
    set<pair<int,int>> ss;
    dsu uf(N);
    for (int i=0;i<M;i++) {
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        all_graph[a].push_back(b);
        all_graph[b].push_back(a);
        if (uf.same(a,b)) {
            s.insert(a);
            s.insert(b);
            ss.insert({a,b});
            ss.insert({b,a});
        } else {
            lca.addEdge(a,b);
            uf.merge(a,b);
        }
    }
    lca.init();
    map<pair<int,int>,int> dists;
    for (auto a:s) {
        auto d = dist(a,N,all_graph);
        for (auto b:s) {
            if (a >= b) continue;
            dists[{a,b}] = d[b];
        }
    }
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int u,v;
        cin >> u >> v;
        u--;
        v--;
        int ret = lca.dist(u,v);
        for (auto t:dists) {
            auto [e,d] = t;
            auto [a,b] = e;
            ret = min(ret,d+lca.dist(u,a)+lca.dist(v,b));
            ret = min(ret,d+lca.dist(u,b)+lca.dist(v,a));
        }
        cout << ret << endl;
    }
}

