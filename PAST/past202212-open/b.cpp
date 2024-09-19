#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int A,B,C,D;
    cin >> A >> B >> C >> D;
    int v1 = A*D;
    int v2 = B*C;
    if (B*D<0) {
        v1 = -v1;
        v2 = -v2;
    }
    if (v1<v2) {
        cout << "<" << endl;
    } else if (v1>v2) {
        cout << ">" << endl;
    } else {
        cout << "=" << endl;
    }
}
