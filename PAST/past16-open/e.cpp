#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string X;
    cin >> X;
    int N = X.size();
    if (X[0]!='1') {
        cout << N << endl;
        return 0;
    }
    bool flag = true;
    for (int i=1;i<N;i++) {
        if (X[i]!='0') {
            flag = false;
            break;
        }
    }
    if (flag) {
        cout << N-1 << endl;
    } else {
        cout << N << endl;
    }
}
