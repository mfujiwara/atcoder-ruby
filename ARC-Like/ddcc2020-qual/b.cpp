#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> acc(N);
    for (int i=0;i<N;i++) {
        long long A;
        cin >> A;
        if (i==0) {
            acc[i] = A;
        } else {
            acc[i] = acc[i-1] + A;
        }
    }
    long long ret = 1000000000000000;
    for (int i=0;i<N-1;i++) {
        ret = min(ret, abs(acc[N-1]-2*acc[i]));
    }
    cout << ret << endl;
}
