#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int A,B,X,Y;
    cin >> A >> B >> X >> Y;
    cout << min(X/A,Y/B) << endl;
}
