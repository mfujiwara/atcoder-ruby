#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

long long op(long long a, long long b) { return (a+b)%1000000007; }
long long e() { return 0; }

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    set<long long>S;
    for (int i=0;i<N;i++) {
        cin>>A[i];
        S.insert(A[i]);
    }
    vector<long long> L(S.begin(), S.end());
    map<long long,int> vtoi;
    for (int i=0;i<L.size();i++) {
        vtoi[L[i]] = i;
    }
    segtree<long long, op, e> upseg(vector<long long>(L.size(), 0));
    segtree<long long, op, e> downseg(vector<long long>(L.size(), 0));
    for (int i=0;i<N;i++) {
        upseg.set(vtoi[A[i]], (upseg.get(vtoi[A[i]])+downseg.prod(0, vtoi[A[i]])+1)%1000000007);
        downseg.set(vtoi[A[i]], (downseg.get(vtoi[A[i]])+upseg.prod(vtoi[A[i]]+1, L.size())+1)%1000000007);
    }
    cout << (upseg.all_prod() + downseg.all_prod() - 2*N + 1000000007) % 1000000007 << endl;
}
