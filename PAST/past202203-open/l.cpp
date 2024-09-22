#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

long long pow(long long base, long long exp, long long mod) {
    long long ret = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            ret = ret * base % mod;
        }
        base = base * base % mod;
        exp /= 2;
    }
    return ret;
}

long long f(long long x, long long a, long long mod) {
    if (a==1) {
        return x;
    }
    long long ret = f(x, a/2, mod);
    ret = ret * (pow(10,a/2,mod)+1) % mod;
    if (a%2==1) {
        ret = (ret * 10 + x) % mod;
    }
    return ret;
}

int main() {
    int K;
    long long M;
    cin >> K >> M;
    long long ret = 0;
    for (int i=0;i<K;i++) {
        long long c,d;
        cin >> c >> d;
        ret = (ret * pow(10,d,M) + f(c,d,M)) % M;
    }
    cout << ret << endl;
}
