#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    dsu d(N);
    for (int i=0;i<N-1;i++) {
        int A,B;
        cin >> A >> B;
        A--;B--;
        if (d.same(A,B)) {
            cout << "No" << endl;
            return 0;
        }
        d.merge(A,B);
    }
    cout << "Yes" << endl;
}
