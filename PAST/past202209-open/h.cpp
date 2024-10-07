#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,X;
    cin >> N >> X;
    tuple<int,int,int> maxi = make_tuple(0,0,0);
    vector<pair<int,int>> dp(X+1,make_pair(0,0));
    dp[X]=make_pair(0,0);
    for (int i=0;i<N;i++) {
        int A,B,C;
        cin >> A >> B >> C;
        for (int j=B;j<=X;j++) {
            auto [x,y] = dp[j];
            dp[j-B]=max(dp[j-B],make_pair(x+C,y-A));
            maxi = max(maxi,make_tuple(x+C,y-A,j-B));
        }
    }
    cout << get<0>(maxi) << " " << 1000000000+get<1>(maxi) << " " << get<2>(maxi) << endl;
}
