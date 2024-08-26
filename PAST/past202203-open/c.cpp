#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string a;
    cin >> a;
    int n = (a.size()-1)/3;
    for (int i=0;i<a.size()-3*n;i++) {
        cout << a[i];
    }
    cout << (char)('a'-1+n) << endl;
}
