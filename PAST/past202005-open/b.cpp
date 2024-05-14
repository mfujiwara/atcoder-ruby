#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,Q;
    cin >> N >> M >> Q;
    vector<int> A(M,N);
    vector<set<int>> S(N,set<int>());
    for (int i=0;i<Q;i++) {
        int t;
        cin >> t;
        if (t == 1) {
            int n;
            cin >> n;
            set<int> s = S[n-1];
            int score = 0;
            for (auto itr = s.begin(); itr != s.end(); ++itr) {
                score += A[*itr];
            }
            cout << score << endl;
        } else {
            int n,m;
            cin >> n >> m;
            A[m-1] -= 1;
            S[n-1].insert(m-1);
        }
    }
}
