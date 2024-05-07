#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;
    vector<int> C(N);
    vector<int> D(N);
    int M=N/2+1;
    vector<long long > dp(M,(long long) pow(10,15));
    dp[0] = 0;
    for (int i=0;i<N;i++) {
        cin >> C[i];
    }
    for (int i=0;i<N;i++) {
        cin >> D[i];
    }
    for (int i=0;i<N;i++) {
        vector<long long > nexts(M);
        for (int j=0;j<M;j++) {
            nexts[j] = dp[j]+D[i];
        }
        if (S[i] == '(') {
            for (int j=1;j<M;j++) {
                if (nexts[j]>dp[j-1]) {
                    nexts[j] = dp[j-1];
                }
            }
            for (int j=0;j<M-1;j++) {
                if (nexts[j]>dp[j+1]+C[i]) {
                    nexts[j] = dp[j+1]+C[i];
                }
            }
        } else {
            for (int j=0;j<M-1;j++) {
                if (nexts[j]>dp[j+1]) {
                    nexts[j] = dp[j+1];
                }
            }
            for (int j=1;j<M;j++) {
                if (nexts[j]>dp[j-1]+C[i]) {
                    nexts[j] = dp[j-1]+C[i];
                }
            }
        }
        dp = nexts;
    }
    cout << dp[0] << endl;
}
