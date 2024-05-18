#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<string> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    string ret = "";
    for (int i=0;i<N;i++) {
        set<char> s;
        set<char> t;
        for (int j=0;j<N;j++) {
            s.insert(A[i][j]);
            t.insert(A[N-1-i][j]);
        }
        set<char> u;
        set_intersection(s.begin(), s.end(), t.begin(), t.end(), inserter(u, u.end()));
        if (u.size() == 0) {
            cout << -1 << endl;
            return 0;
        }
        char c = 'z';
        for (auto x:u) {
            c = min(c,x);
        }
        ret += c;
    }
    cout << ret << endl;    
}
