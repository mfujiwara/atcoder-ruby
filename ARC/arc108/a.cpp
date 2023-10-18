#include <bits/stdc++.h>
using namespace std;

vector<long long> calc_divisors(long long N) {
    vector<long long> res;

    for (long long i = 1; i * i <= N; ++i) {
        if (N % i != 0) continue;
        res.push_back(i);
        if (N / i != i) res.push_back(N / i);
    }

    sort(res.begin(), res.end());
    return res;
}

int main() {
    long long S,P;
    cin >> S >> P;
    vector<long long> divisors = calc_divisors(P);
    for (int i=0;i<divisors.size();i++) {
        long long a = divisors[i];
        long long b = P/a;
        if (a+b==S) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
