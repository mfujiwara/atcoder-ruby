#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

vector<int> z_algorithm(vector<string> s) {
    int N = s.size();
    vector<int> z(N);
    z[0] = N;
    int i = 1, j = 0;
    while (i<N) {
        while (i+j<N && s[j]==s[i+j]) ++j;
        z[i] = j;
        if (j==0) {++i; continue;}
        int k = 1;
        while (i+k<N && k+z[k]<j) z[i+k] = z[k], ++k;
        i += k; j -= k;
    }
    return z;
}

int main() {
    int H,W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0;i<H;i++) {
        cin >> S[i];
    }
    vector<string> T(H);
    for (int i=0;i<H;i++) {
        cin >> T[i];
    }
    vector<string> U(W*3);
    for (int i=0;i<W;i++) {
        for (int j=0;j<H;j++) {
            U[i] += S[j][i];
        }
    }
    vector<string> invT(W);
    for (int i=0;i<W;i++) {
        for (int j=0;j<H;j++) {
            U[i+W] += T[j][i];
            U[i+2*W] += T[j][i];
        }
    }
    vector<int> z = z_algorithm(U);
    for (int i=0;i<W;i++) {
        if (z[W+i]>=W) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
}
