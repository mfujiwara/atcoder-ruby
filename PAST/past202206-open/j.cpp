#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string S,T;
    cin >> S >> T;
    tuple<int,int,int> s = {
        (S[0]-'0')*1000+(S[1]-'0')*100+(S[2]-'0')*10+(S[3]-'0'),
        (S[5]-'0')*10+(S[6]-'0'),
        (S[8]-'0')*10+(S[9]-'0')
    };
    tuple<int,int,int> t = {
        (T[0]-'0')*1000+(T[1]-'0')*100+(T[2]-'0')*10+(T[3]-'0'),
        (T[5]-'0')*10+(T[6]-'0'),
        (T[8]-'0')*10+(T[9]-'0')
    };
    tuple<int,int,int> now = {2022,1,1};
    int ans = 0;
    int day = 0;
    while (now <= t) {
        if (s<=now && now<=t && day<=1) {
            ans++;
        }

        vector<int> next = {get<0>(now),get<1>(now),get<2>(now)};
        next[2]++;
        if (next[2] == 32 || ((next[1]==4||next[1]==6||next[1]==9||next[1]==11)&&next[2]==31) || (next[1]==2&&next[2]==30) || (next[1]==2&&next[2]==29 && ((next[0]%4!=0||next[0]%100==0)&&next[0]%400!=0))) {
            next[2] = 1;
            next[1]++;
        }
        if (next[1] == 13) {
            next[1] = 1;
            next[0]++;
        }
        now = {next[0],next[1],next[2]};
        day++;
        day %= 7;
    }
    cout << ans << endl;
}
