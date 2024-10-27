#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    set<long long> s;
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        s.insert(a);
    }
    int Q;
    cin >> Q;
    for (int i=0;i<Q;i++) {
        int M;
        cin >> M;
        int cnt=0;
        for (int j=0;j<M;j++) {
            long long b;
            cin >> b;
            if (s.find(b) != s.end()) {
                cnt++;
            }
        }
        cout << N+M-cnt << endl;
    }
}
