#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    double a,b,c;
    cin >> a >> b >> c;
    double l = 1;
    double r = 2;
    while (r-l>1e-10) {
        double m = (l+r)/2;
        double v = a*m*m*m*m*m+b*m+c;
        if (v>0) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << fixed << setprecision(10);
    cout << l << endl;
}
