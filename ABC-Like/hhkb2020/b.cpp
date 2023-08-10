#include <bits/stdc++.h>
using namespace std;

int main() {
    int H,W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0;i<H;i++) {
        cin >> S[i];
    }
    int ret=0;
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (S[i][j]=='.' && j+1<W && S[i][j+1]=='.') {
                ret++;
            }
            if (S[i][j]=='.' && i+1<H && S[i+1][j]=='.') {
                ret++;
            }
        }
    }
    cout << ret << endl;
}
