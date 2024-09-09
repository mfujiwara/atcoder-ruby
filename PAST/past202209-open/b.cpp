#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string N;
    cin >> N;
    int l = N.size();
    if (l<=2) {
        cout << 0 << endl;
    } else {
        cout << N.substr(0,l-2) << endl;
    }
}
