#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long N;
    cin >> N;
    long long base = 1;
    vector<long long> rets = {};
    while (N!=0) {
        long long d = N%3;
        if (d==2) {
            rets.push_back(-base);
            N++;
        } else if (d==1) {
            rets.push_back(base);
        }
        N /= 3;
        base *= 3;
    }
    cout << rets.size() << endl;
    cout << rets[0];
    for (int i=1;i<rets.size();i++) {
        cout << " " << rets[i];
    }
    cout << endl;
}
