#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int op(int a, int b) { return max(a, b); }
int e() { return 0; }

int main() {
    int N;
    long long L;
    cin >> N >> L;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    long long ok=1;
    long long ng=L+1;
    while (ng-ok>1) {
        long long mid = (ok+ng)/2;
        segtree<int, op, e> seg(vector<int>(N+1,0));
        seg.set(0,1);
        vector<long long> sums(0);
        sums.push_back(0);
        for (int i=0;i<N;i++) {
            sums.push_back(sums.back()+A[i]);
            long long maxi = sums.back()-mid+1;
            long long mini = sums.back()-L;
            int maxi_idx = lower_bound(sums.begin(),sums.end(),maxi)-sums.begin();
            int mini_idx = lower_bound(sums.begin(),sums.end(),mini)-sums.begin();
            if (maxi_idx>mini_idx) {
                int p = seg.prod(mini_idx,maxi_idx);
                if (p>0) {
                    seg.set(i+1,1);
                }
            }
        }
        if (seg.prod(N,N+1)>0) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}
