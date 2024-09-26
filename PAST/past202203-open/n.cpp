#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<long long> P(200000);
    vector<long long> Q(200000);
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        P[a-1]++;
        Q[200000-a]++;
    }
    vector<long long> R = convolution_ll(P,Q);
    int ret = 0;
    for (int i=0;i<R.size();i++) {
        if (R[i] > 0) {
            ret++;
        }
    }
    cout << ret << endl;
}
