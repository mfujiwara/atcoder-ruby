#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> A(N);
    for (int i=0;i<N;i++) {
        int k;
        cin >> k;
        for (int j=0;j<k;j++) {
            int a;
            cin >> a;
            A[i].insert(a);
        }
    }
    int P,Q;
    cin >> P >> Q;
    vector<int> B(P);
    for (int i=0;i<P;i++) {
        cin >> B[i];
    }
    int ret = 0;
    for (int i=0;i<N;i++) {
        int cnt = 0;
        for (int j=0;j<P;j++) {
            if (A[i].count(B[j])) {
                cnt++;
            }
        }
        if (cnt >= Q) {
            ret++;
        }
    }
    cout << ret << endl;
}
