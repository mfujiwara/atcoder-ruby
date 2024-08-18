#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S,T;
    cin >> S >> T;
    vector<vector<int>> dp(S.size()+1, vector<int>(T.size()+1, 0));
    for (int i=0;i<S.size();i++) {
        for (int j=0;j<T.size();j++) {
            if (S[i]==T[j]) {
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j]);
            } else {
                dp[i+1][j+1]=dp[i][j]+1;
            }
        }
    }
    cout << dp[S.size()][T.size()] << endl;
}
