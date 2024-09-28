#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<long long> A(100000,0);
    vector<long long> B(100000,0);
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        A[a-1]++;
        B[100000-a]++;
    }
    vector<long long> c = convolution<998244353>(A, B);
    vector<long long> S(N);
    for (int i=0;i<N;i++) {
        cin >> S[i];
    }
    long long fact = 1;
    for (int i=1;i<N-1;i++) {
        fact = fact*i%998244353;
    }
    long long ret = 0;
    for (int i=1;i<N;i++) {
        long long score = c[99999+i]*fact%998244353;
        score = score*S[i-1]%998244353;
        score = score*(N-i)%998244353;
        ret = (ret+score)%998244353;
    }
    cout << ret << endl;
}
