#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long A,B,X;
    cin >> A >> B >> X;
    long long l = min(X/A,1000000000);
    while (true) {
        long long d = 0;
        long long t = l;
        while (t>0) {
            d += t%10;
            t /= 10;
        }
        if (A*l+B*d<=X) {
            cout << l << endl;
            return 0;
        }
        l--;
    }
}
