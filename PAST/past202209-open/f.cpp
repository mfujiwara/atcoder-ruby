#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    vector<set<int>> X(200001);
    for (int i=0;i<N;i++) {
        int c;
        cin >> c;
        for (int j=0;j<c;j++) {
            int x;
            cin >> x;
            X[x].insert(i);
        }
    }
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int d;
        cin >> d;
        set<int> xxx;
        for (int j=0;j<d;j++) {
            int y;
            cin >> y;
            for (int x : X[y]) {
                xxx.insert(x);
            }
        }
        pair<int,int> ret = {-2,-2};
        for (int i=0;i<N;i++) {
            if (xxx.count(i) == 0) {
                ret = max(ret, {A[i],i});
            }
        }
        cout << ret.second+1 << endl;
    }
}
