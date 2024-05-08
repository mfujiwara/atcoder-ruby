#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

pair<long long,int> op(pair<long long,int> a, pair<long long,int> b) {
    if (a.first == b.first) {
        return a.second < b.second ? a : b;
    } else {
        return a.first < b.first ? a : b;
    }
}
pair<long long,int> e() { return make_pair((long long)pow(10,10),-1); }
int main() {
    int N,K,D;
    cin >> N >> K >> D;
    if (D*(K-1) >= N) {
        cout << -1 << endl;
        return 0;
    }
    vector<pair<long long,int>> A(N);
    long long a;
    for (int i=0;i<N;i++) {
        cin>>a;
        A[i] = make_pair(a,i);
    }
    vector<long long> rets(K);
    int s=0;
    segtree<pair<long long,int>, op, e> seg(A);
    for (int i=0;i<K;i++) {
        pair<long long,int> t = seg.prod(s,N-D*(K-1-i));
        rets[i] = t.first;
        s = t.second+D;
    }
    for (int i=0;i<K;i++) {
        cout << rets[i];
        if (i<K-1) cout << " ";
    }
    cout << endl;
}
