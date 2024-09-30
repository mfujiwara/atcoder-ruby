#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

vector<vector<int>> next_char(string S){
    int n=S.size();
    vector<vector<int>> res(n+1,vector<int>(26,n));
    for (int i = n-1; i>=0; i--){
        for (int j = 0; j<26; j++){
            res[i][j]=res[i+1][j];
        }
        res[i][S[i]-'a']=i;
    }
    return res;
}

int main() {
    string S,T;
    cin >> S >> T;
    int K;
    cin >> K;
    auto next_s = next_char(S);
    auto next_t = next_char(T);

    int n = S.size();
    int m = T.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1,0));
    for (int r=0;r<=K;r++) {
        vector<vector<int>> next_dp(n+1, vector<int>(m+1,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 26; k++) {
                    if (next_s[i][k] < n && next_t[j][k] < m) {
                        next_dp[next_s[i][k]+1][next_t[j][k]+1] = max(next_dp[next_s[i][k]+1][next_t[j][k]+1],next_dp[i][j]+1);
                    }
                    if (r>0 && next_t[j][k]<m) {
                        next_dp[i+1][next_t[j][k]+1] = max(next_dp[i+1][next_t[j][k]+1],dp[i][j]+1);
                    }
                }
            }
        }
        dp = next_dp;
    }
    int ret = 0;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            ret = max(ret, dp[i][j]);
        }
    }
    cout << ret << endl;
}
