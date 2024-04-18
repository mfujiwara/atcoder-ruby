#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

long long op(long long a, long long b) { return min(a, b); }

long long e() { return pow(10,9); }

int main() {
    int N;
    cin >> N;
    int N_even = (N + 1) / 2;
    vector<long long> C_even(N);
    vector<long long> C_odd(N);
    long long tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        if (i % 2 == 0) {
            C_even[i] = tmp;
            C_odd[i] = pow(10,9);
        } else {
            C_odd[i] = tmp;
            C_even[i] = pow(10,9);
        }
    }
    segtree<long long, op, e> seg_even(C_even);
    segtree<long long, op, e> seg_odd(C_odd);
    long long even = 0;
    long long odd = 0;
    long long ret = 0;
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int tmp;
        cin >> tmp;
        if (tmp==1) {
            long long x,a;
            cin >> x >> a;
            x-=1;
            if (x%2==0) {
                int v=seg_even.get(x);
                if (v-even>=a) {
                    seg_even.set(x,v-a);
                    ret+=a;
                }
            } else {
                int v=seg_odd.get(x);
                if (v-odd>=a) {
                    seg_odd.set(x,v-a);
                    ret+=a;
                }
            }
        } else if (tmp==2) {
            long long a;
            cin >> a;
            if (seg_even.all_prod()-even>=a) {
                even+=a;
                ret+=a*N_even;
            }
        } else {
            long long a;
            cin >> a;
            if (seg_odd.all_prod()-odd>=a && seg_even.all_prod()-even>=a) {
                odd+=a;
                even+=a;
                ret+=a*N;
            }
        }
    }
    cout << ret << endl;
}
