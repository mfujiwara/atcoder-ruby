#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<unsigned long long> A(N);
    unsigned long long maxi = 0;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        maxi = max(maxi, A[i]);
    }
    for (int i=0;i<N;i++) {
        unsigned long long v = A[i]*10000000000/maxi;
        unsigned long long q = v%10;
        v /= 10;
        if (q >= 5) {
            v++;
        }
        cout << v;
        if (i < N-1) {
            cout << " ";
        } else {
            cout << endl;
        }
    }
}
