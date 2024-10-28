#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

vector<vector<pair<int,long long>>> G;

long long calc(int u, int p, long long l,long long r,long long N) {
    long long ret= (l+1)*(N-1-r);
    for (auto [v,id]:G[u]) {
        if (v==p) continue;
        ret+=calc(v,u,min(l,id),max(r,id),N);
    }
    return ret;
}

int main() {
    long long N;
    cin >> N;
    G = vector<vector<pair<int,long long>>>(N);
    for (long long i=0;i<N-1;i++) {
        int u,v;
        cin >> u >> v;
        u--;
        v--;
        G[u].push_back(make_pair(v,i));
        G[v].push_back(make_pair(u,i));
    }
    long long ret = N*(N-1)/2;
    for (auto [v,id]:G[0]) {
        ret+=calc(v,0,id,id,N);
    }
    cout << ret << endl;
}
