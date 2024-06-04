#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M,K;
    cin >> N >> M >> K;
    vector<string> S(N);
    for (int i=0;i<N;i++) {
        cin >> S[i];
    }
    for (int t=min(N,M);t>0;t--) {
        for (int i=0;i<N;i++) {
            if (i+t-1>=N) {
                break;
            }
            for (int j=0;j<M;j++) {
                if (j+t-1>=M) {
                    break;
                }
                vector<int> counts(10);
                for (int k=0;k<t;k++) {
                    for (int l=0;l<t;l++) {
                        counts[S[i+k][j+l]-'0']++;
                    }
                }
                int max_count = *max_element(counts.begin(),counts.end());
                if (max_count + K>=t*t) {
                    cout << t << endl;
                    return 0;
                }
            }
        }
    }
}
