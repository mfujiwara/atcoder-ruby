#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S,T;
    cin >> N >> S >> T;
    vector<vector<int>> dp = vector<vector<int>>(N,vector<int>(N,0));
    for (int d=2;d<N;d++) {
        for (int i=0;i+d<N;i++) {
            int j = i+d;
            dp[i][j] = max(dp[i][j],dp[i+1][j]);
            dp[i][j] = max(dp[i][j],dp[i+1][j-1]);
            for (int k=i;k<j;k++) {
                dp[i][j] = max(dp[i][j],dp[i][k]+dp[k+1][j]);
            }
            if (d%3==2 && S[i]==T[0] && S[j]==T[2]) {
                int k=i+1;
                while (k<j) {
                    if (S[k]==T[1] && (k==i+1 || dp[i+1][k-1]==(k-i-1)/3) && (j==k+1 || dp[k+1][j-1]==(j-k-1)/3)) {
                        dp[i][j] = max(dp[i][j],(d+1)/3);
                    }
                    k+=3;
                }
            }
        }
    }
    cout << dp[0][N-1] << endl;
}
