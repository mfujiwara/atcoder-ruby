#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<long long>> A(H,vector<long long>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> A[i][j];
        }
    }
    vector<vector<vector<long long>>> dp(H,vector<vector<long long>>(W,vector<long long>(H+W,0)));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            for (int k=1;k<i+j+2;k++) {
                if (i == 0 && j == 0) {
                    dp[i][j][k] = A[i][j];
                } else if (i==0) {
                    dp[i][j][k] = max(dp[i][j-1][k-1]+A[i][j],dp[i][j-1][k]);
                } else if (j==0) {
                    dp[i][j][k] = max(dp[i-1][j][k-1]+A[i][j],dp[i-1][j][k]);
                } else {
                    long long v1 = max(dp[i-1][j][k-1]+A[i][j],dp[i-1][j][k]);
                    long long v2 = max(dp[i][j-1][k-1]+A[i][j],dp[i][j-1][k]);
                    dp[i][j][k] = max(v1,v2);
                }
            }
        }
    }
    for (int i=1;i<=H+W-1;i++) {
        cout << dp[H-1][W-1][i] << endl;
    }
}
