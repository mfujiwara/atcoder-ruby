#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W;
    cin >> H >> W;
    vector<vector<int>> S(H,vector<int>(W));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> S[i][j];
        }
    }
    vector<vector<int>> queue(W,vector<int>(H));
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            queue[j][H-i-1] = S[i][j];
        }
    }
    int N;
    cin >> N;
    for (int i=0;i<N;i++) {
        int r,c;
        cin >> r >> c;
        queue[c-1].erase(queue[c-1].begin()+H-r);
        queue[c-1].push_back(0);
    }
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cout << queue[j][H-i-1];
            if (j != W-1) {
                cout << " ";
            } else {
                cout << endl;
            }
        }
    }
}
