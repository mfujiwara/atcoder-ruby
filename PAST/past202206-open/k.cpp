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

long long substr(string s, vector<vector<int>> next) {
    int n = s.size();
    vector<long long> dp(n + 1);
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 26; j++) {
            if (next[i][j] < n) {
                dp[next[i][j] + 1] += dp[i];
                dp[next[i][j] + 1] %= 998244353;
            }
        }
    }
    long long res = 0;
    for (int i = 0; i <= n; i++) {
        res += dp[i];
        res %= 998244353;
    }
    return res;
}

long long substr(string s, string t, vector<vector<int>> next_s, vector<vector<int>> next_t) {
    int n = s.size(), m = t.size();
    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1));
    dp[0][0] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < 26; k++) {
                if (next_s[i][k] < n && next_t[j][k] < m) {
                    dp[next_s[i][k] + 1][next_t[j][k] + 1] += dp[i][j];
                    dp[next_s[i][k] + 1][next_t[j][k] + 1] %= 998244353;
                }
            }
        }
    }
    long long res = 0;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            res += dp[i][j];
            res %= 998244353;
        }
    }
    return res;
}

int main() {
    long long MOD = 998244353;
    string S,T;
    cin >> S >> T;
    auto next_s = next_char(S);
    auto next_t = next_char(T);
    long long ret = substr(S, next_s) + substr(T, next_t) - substr(S, T, next_s, next_t) -1;
    ret += MOD;
    ret %= MOD;
    cout << ret << endl;
}
