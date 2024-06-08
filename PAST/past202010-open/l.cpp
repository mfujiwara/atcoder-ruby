#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<long long> h(N);
    map<long long,int> oddDiffs;
    map<long long,int> evenDiffs;
    for (int i=0;i<N;i++) {
        cin >> h[i];
        if (i==0) {
            continue;
        }
        if (i%2 == 0) {
            oddDiffs[h[i]-h[i-1]]++;
        } else {
            evenDiffs[h[i]-h[i-1]]++;
        }
    }
    long long evenBase = 0;
    for (int i=0;i<Q;i++) {
        int t,u,v;
        cin >> t;
        if (t == 1) {
            cin >> v;
            evenBase += v;
        } else if (t == 2) {
            cin >> v;
            evenBase -= v;
        } else {
            cin >> u >> v;
            u--;
            if (u == 0) {
                evenDiffs[h[1]-h[0]]--;
                h[0] += v;
                evenDiffs[h[1]-h[0]]++;
            } else if (u == N-1) {
                if (N%2 == 0) {
                    evenDiffs[h[N-1]-h[N-2]]--;
                    h[N-1] += v;
                    evenDiffs[h[N-1]-h[N-2]]++;
                } else {
                    oddDiffs[h[N-1]-h[N-2]]--;
                    h[N-1] += v;
                    oddDiffs[h[N-1]-h[N-2]]++;
                }
            } else {
                if (u%2 == 0) {
                    evenDiffs[h[u+1]-h[u]]--;
                    oddDiffs[h[u]-h[u-1]]--;
                    h[u] += v;
                    evenDiffs[h[u+1]-h[u]]++;
                    oddDiffs[h[u]-h[u-1]]++;
                } else {
                    oddDiffs[h[u+1]-h[u]]--;
                    evenDiffs[h[u]-h[u-1]]--;
                    h[u] += v;
                    oddDiffs[h[u+1]-h[u]]++;
                    evenDiffs[h[u]-h[u-1]]++;
                }
            }
        }
        cout << evenDiffs[evenBase]+oddDiffs[-evenBase] << endl;
    }
}
