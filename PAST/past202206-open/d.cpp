#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    dsu d(26);
    for (int i=0;i<N;i++) {
        string a,b;
        cin >> a >> b;
        d.merge(a[0]-'a',b[0]-'a');
    }
    string S,T;
    cin >> S >> T;
    for (int i=0;i<S.size();i++) {
        if (d.same(S[i]-'a',T[i]-'a')) {
            continue;
        } else {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}
