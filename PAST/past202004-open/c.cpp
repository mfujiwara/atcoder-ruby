#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<string> S(N);
    for (int i=0;i<N;i++) {
        cin >> S[i];
    }
    for (int i=N-2;i>=0;i--) {
        for (int j=1;j<2*N-2;j++) {
            if (S[i][j] == '#'&&(S[i+1][j-1]=='X'||S[i+1][j]=='X'||S[i+1][j+1]=='X')) {
                S[i][j] = 'X';
            }
        }
    }
    for (int i=0;i<N;i++) {
        cout << S[i] << endl;
    }
}
