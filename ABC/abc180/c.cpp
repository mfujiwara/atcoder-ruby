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
    long long N;
    cin >> N;
    vector<long long> divs = calc_divisors(N);
    for (int i=0;i<divs.size();i++) {
        cout << divs[i] << endl;
    }
}
