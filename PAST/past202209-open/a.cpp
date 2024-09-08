#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int X,Y,Z;
    cin >> X >> Y >> Z;
    cout << max(Z+X,Y) << endl;
}
