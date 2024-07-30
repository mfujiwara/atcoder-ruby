#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

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
    int X,Y;
    cin >> X >> Y;
    int xc = calc_divisors(X).size();
    int yc = calc_divisors(Y).size();
    if (xc > yc) {
        cout << "X" << endl;
    } else if (xc < yc) {
        cout << "Y" << endl;
    } else {
        cout << "Z" << endl;
    }
}
