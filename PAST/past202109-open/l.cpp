#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long N,K;
    cin >> N >> K;
    vector<long long> sums = vector<long long>(1,0);
    for (long long i=0;i<N;i++) {
        long long a;
        cin >> a;
        sums.push_back(sums[i]+a);
    }
    sort(sums.begin(), sums.end());
    long long ok = 1e18;
    long long ng = -1;
    while (ok-ng>1) {
        long long mid = (ok+ng)/2;
        long long cnt = 0;
        long long j=0;
        for (long long i=0;i<N;i++) {
            while (j+1<=N && sums[j+1]-sums[i]<=mid) {
                j++;
            }
            cnt += j-i;
        }
        if (cnt>=K) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}
