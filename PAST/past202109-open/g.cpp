#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    long long K;
    cin >> N >> K;
    vector<tuple<long long,long long,long long>> abc(N);
    for (int i=0;i<N;i++) {
        long long a,b,c;
        cin >> a >> b >> c;
        abc[i] = make_tuple(a,b,c);
    }
    long long ok = 1e18;
    long long ng = 0;
    while (ng+1!=ok) {
        long long mid = (ok+ng)/2;
        long long cnt = 0;
        for (int i=0;i<N;i++) {
            long long a,b,c;
            tie(a,b,c) = abc[i];
            if (mid < b) {
                continue;
            }
            cnt += min(a,(mid-b)/c+1);
        }

        if (cnt >= K) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}
