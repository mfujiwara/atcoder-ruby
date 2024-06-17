#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int H,W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0;i<H;i++) {
        cin>>S[i];
    }
    vector<vector<char>> A(H,vector<char>(W));
    vector<vector<char>> B(H,vector<char>(W));
    vector<vector<char>> C(W,vector<char>(H));
    vector<vector<char>> D(W,vector<char>(H));
    string t;
    for (int i=0;i<H;i++) {
        cin>>t;
        for (int j=0;j<W;j++) {
            A[i][j] = t[j];
            B[H-1-i][W-1-j] = t[j];
            C[W-1-j][i] = t[j];
            D[j][H-1-i] = t[j];
        }
    }
    vector<vector<vector<char>>> T = {A,B,C,D};
    for (int x=-9;x<=9;x++) {
        for (int y=-9;y<=9;y++) {
            for (int t=0;t<4;t++) {
                bool ok = true;
                auto U = T[t];
                for (int i=0;i<U.size();i++) {
                    for (int j=0;j<U[i].size();j++) {
                        int ni = i+x;
                        int nj = j+y;
                        if (ni<0 || ni>=H || nj<0 || nj>=W) {
                            if (U[i][j]=='#') {
                                ok = false;
                            }
                        } else {
                            if (U[i][j]=='#' && S[ni][nj]=='#') {
                                ok = false;
                            }
                        }
                        if (!ok) break;
                    }
                    if (!ok) break;
                }
                if (ok) {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "No" << endl;
}
