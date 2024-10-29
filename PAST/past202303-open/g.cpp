#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<int>> A(H,vector<int>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> A[i][j];
        }
    }
    set<pair<int,int>> rets;
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (i>0) {
                int a = A[i][j];
                int b = A[i-1][j];
                if (a<b) {
                    rets.insert({a,b});
                } else {
                    rets.insert({b,a});
                }
            }
            if (j>0) {
                int a = A[i][j];
                int b = A[i][j-1];
                if (a<b) {
                    rets.insert({a,b});
                } else {
                    rets.insert({b,a});
                }
            }
        }
    }
    for (auto [a,b]:rets) {
        cout << a << " " << b << endl;
    }
}
