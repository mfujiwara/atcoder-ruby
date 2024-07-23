#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

long long op(long long a, long long b) {
    return min(a,b);
}
long long e() { 
    return 1e10; 
}
int main() {
    int N,Q;
    cin >> N >> Q;
    map<long long,set<int>> memo;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
        memo[A[i]].insert(i);
    }
    segtree<long long,op,e> seg(A);
    for (int i=0;i<Q;i++) {
        int t,x;
        long long y;
        cin >> t >> x >> y;
        x-=1;
        if (t == 1) {
            auto v = seg.prod(x,x+1);
            memo[v].erase(x);
            seg.set(x,y);
            memo[y].insert(x);
        } else {
            auto v = seg.prod(x,y);
            auto it = memo[v].lower_bound(x);
            vector<int> arr;
            while (it != memo[v].end() && *it < y) {
                arr.push_back(*it);
                it++;
            }
            cout << arr.size();
            for (int i=0;i<arr.size();i++) {
                cout << " " << arr[i]+1;
            }
            cout << endl;
        }
    }
}
