#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,K;
    cin >> N >> K;
    vector<int> A(N);
    vector<int> counts(1000001);
    for (int i=0;i<N;i++) {
        cin >> A[i];
        counts[A[i]]+=1;
    }
    int ret = 1;
    for (int i=2;i<=1000000;i++) {
        int sum = 0;
        for (int j=i;j<=1000000;j+=i) {
            sum += counts[j];
        }
        if (sum>=K) {
            ret = i;
        }
    }
    cout << ret << endl;
}
