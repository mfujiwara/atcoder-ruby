#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int op(int a, int b) { return (a+b)%2; }
int e() { return 0; }

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<int> a(N);
    segtree<int, op, e> seg(a);
    for (int i=0;i<Q;i++) {
        int t,x;
        cin >> t >> x;
        if (t==1) {
            int d = x>N ? x-N : N-x+1;
            auto v = seg.prod(d-1,N);
            if (v%2==0) {
                cout << x << endl;
            } else {
                x = x>N ? x-d*2+1 : x+d*2-1;
                cout << x << endl;
            }
        } else {
            auto v = seg.get(x-1);
            seg.set(x-1, 1-v);
        }
    }
}
