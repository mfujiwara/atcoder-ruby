#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W,N;
    cin >> H >> W >> N;
    vector<vector<int>> A(H,vector<int>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> A[i][j];
            A[i][j]-=1;
        }
    }
    vector<int> C(N);
    for (int i=0;i<N;i++) {
        cin >> C[i];
    }
    for (int i=0;i<H;i++) {
        for (int j=0;j<W-1;j++) {
            int a=A[i][j];
            int b=A[i][j+1];
            if (a!=b && C[a]==C[b]) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    for (int i=0;i<H-1;i++) {
        for (int j=0;j<W;j++) {
            int a=A[i][j];
            int b=A[i+1][j];
            if (a!=b && C[a]==C[b]) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
}
