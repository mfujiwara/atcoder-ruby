#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    long long N;
    cin >> N;
    long long sq = (long long)sqrt(N);
    if (sq*sq<N) {
        sq++;
    }
    N -= (sq-1)*(sq-1);
    if (N<=sq) {
        cout << sq+1-N << endl;
    } else {
        cout << N-sq+1 << endl;
    }
}
