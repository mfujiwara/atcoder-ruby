#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    set<long long> A;
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        A.insert(a);
    }
    set<int> ret;
    for (int i=0;i<=M;i++) {
        long long b;
        cin >> b;
        if (A.find(b) != A.end()) {
            ret.insert(b);
        }
    }
    for (auto r:ret) {
        cout << r;
        if (r != *ret.rbegin()) {
            cout << " ";
        }
    }
    cout << endl;
}
