#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int op(int a, int b) { return max(a, b); }
int e() { return 0; }

int main() {
    int N;
    long long P;
    cin >> N >> P;
    vector<pair<long long,int>> A(N);
    for (long i=0;i<N;i++) {
        cin >> A[i].first;
        if (A[i].first<N-1-i || A[i].first+i>P) {
            A[i].first = 1;
        } else {
            A[i].first = -A[i].first - i;
        }
        A[i].second = i;
    }
    sort(A.begin(), A.end());
    segtree<int, op, e> seg(vector<int>(N, 0));
    for (int i=0;i<N;i++) {
        auto [a, index] = A[i];
        if (a>0) break;
        if (index==0) {
            seg.set(index, 1);
        } else {
            seg.set(index, seg.prod(0, index)+1);
        }
    }
    cout << N-seg.all_prod() << endl;
}
