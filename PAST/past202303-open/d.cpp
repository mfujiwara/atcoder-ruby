#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long H,A,B,C,D;
    cin >> H >> A >> B >> C >> D;
    long long base = 0;
    long long ret = 1000000000000000000;
    while (H>0) {
        ret = min(ret, base + (H+A-1)/A*B);
        H = (H-C+1)/2;
        base +=D;
    }
    ret = min(ret, base);
    cout << ret << endl;
}
