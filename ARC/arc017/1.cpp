#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;
    // 素数判定
    bool is_prime = true;
    for (long long i = 2; i * i <= N; ++i) {
        if (N % i == 0) {
            is_prime = false;
            break;
        }
    }
    if (is_prime) cout << "YES" << endl;
    else cout << "NO" << endl;
}
