#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long N, A, B, C, D;
    cin >> N >> A >> B >> C >> D;
    string X;
    cin >> X;
    long long x = (X[0]-'0'-1)*1000 + (X[2]-'0')*100 + (X[3]-'0')*10 + (X[4]-'0');
    // (E+mid)/(N+mid) <= X = (x+1000)/1000
    // (E+mid)*1000 <= (x+1000)*(N+mid)
    // (E+mid)*1000 <= x*N + x*mid + 1000*N + 1000*mid
    // E*1000 + mid*1000 <= x*N + 1000*N + x*mid + 1000*mid
    // (N + B + C*2 + D*3)*1000 <= x*N + 1000*N + x*mid
    // (B + C*2 + D*3)*1000 <= x*N + x*ret
    // ret >= (B + C*2 + D*3)*1000 / x - N
    long long ret = ((B + C*2 + D*3)*1000 + x -1 )/ x - N;
    if (ret < 0) {
        cout << 0 << endl;
    } else {
        cout << ret << endl;
    }
}
