#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    long long total = 0;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        total += A[i];
        total %= 1000000007;
    }
    long long ret = 0;
    for (int i=0;i<N;i++) {
        total -= A[i];
        if (total < 0) total += 1000000007;
        ret += A[i] * total % 1000000007;
        ret %= 1000000007;
    }
    cout << ret << endl;
}
