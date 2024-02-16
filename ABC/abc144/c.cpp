#include <bits/stdc++.h>
using namespace std;

vector<long long> calc_divisors(long long N);

int main() {
    long long N;
    cin >> N;
    vector<long long> divisors = calc_divisors(N);
    int size = divisors.size();
    if (size % 2 == 0) {
        cout << divisors[size / 2] + divisors[size / 2 - 1] - 2 << endl;
    } else {
        cout << divisors[size / 2] * 2 - 2 << endl;
    }
}

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
