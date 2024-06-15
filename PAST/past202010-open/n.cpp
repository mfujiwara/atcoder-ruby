#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    vector<string> S(19);
    S[18] = "000000";
    for (int i=0;i<18;i++) {
        cin >> S[i];
    }
    vector<long long> dp(1<<12,0);
    dp[0] = 1;
    for (int i=0;i<19;i++) {
        vector<long long> dp2(1<<12,0);
        for (int bit0=0;bit0<1<<12;bit0++) {
            if (dp[bit0]==0) continue;
            int tmp = bit0;
            vector<int> row0 = {0,0,0,0,0,0};
            vector<int> row1 = {0,0,0,0,0,0};
            for (int j=0;j<6;j++) {
                row0[j] = tmp%2;
                tmp /= 2;
            }
            for (int j=0;j<6;j++) {
                row1[j] = tmp%2;
                tmp /= 2;
            }
            for (int bit=0;bit<1<<6;bit++) {
                int tmp = bit;
                vector<int> row2 = {0,0,0,0,0,0};
                for (int j=0;j<6;j++) {
                    row2[j] = tmp%2;
                    tmp /= 2;
                }
                bool ok = true;
                for (int j=0;j<6;j++) {
                    if (S[i][j]=='1' && row2[j]==0) {
                        ok = false;
                        break;
                    }
                    if (S[i][j]=='0' && row2[j]==1) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                for (int j=0;j<6;j++) {
                    int t = row1[j];
                    int c = 0;
                    if (t==0) {
                        if (row0[j]==0) c++;
                        if (row2[j]==0) c++;
                        if (j==0 || row1[j-1]==0) c++;
                        if (j==5 || row1[j+1]==0) c++;
                    } else {
                        if (row0[j]==1) c++;
                        if (row2[j]==1) c++;
                        if (j>0 && row1[j-1]==1) c++;
                        if (j<5 && row1[j+1]==1) c++;
                    }
                    if (c<2) {
                        ok = false;
                        break;
                    }
                }
                if (!ok) continue;
                dp2[(bit<<6)|(bit0>>6)] += dp[bit0];
            }
        }
        dp = dp2;
    }
    long long ret = 0;
    for (int bit=0;bit<1<<12;bit++) {
        ret += dp[bit];
    }
    cout << ret << endl;
}
