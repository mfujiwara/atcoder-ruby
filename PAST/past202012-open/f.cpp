#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> A(M);
    for (int i=0;i<M;i++) {
        int a,b,c;
        cin >> a >> b >> c;
        a--;b--;c--;
        A[i] = {a,b,c};
    }
    int ret = 0;
    for (int bit=3;bit<(1<<N);bit++) {
        set<int> B;
        for (int i=0;i<N;i++) {
            if (bit & (1<<i)) {
                B.insert(i);
            }
        }
        set<int> C;
        for (int i=0;i<M;i++) {
            vector<int> v_intersection;
            set_intersection(A[i].begin(), A[i].end(), B.begin(), B.end(),back_inserter(v_intersection));
            if (v_intersection.size() == 2) {
                for (int a : A[i]) {
                    if (B.find(a) == B.end()) {
                        C.insert(a);
                    }
                }
            } else if (v_intersection.size() == 3) {
                C = {};
                break;
            }
        }
        ret = max(ret, (int)C.size());
    }
    cout << ret << endl;
}
