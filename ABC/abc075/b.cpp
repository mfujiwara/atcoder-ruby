#include <bits/stdc++.h>
using namespace std;

int main() {
    int H,W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0;i<H;i++) {
        cin >> S[i];
    }
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            if (S[i][j] == '#') {
                cout << '#';
            } else {
                int count = 0;
                for (int x=i-1;x<i+2;x++) {
                    for (int y=j-1;y<j+2;y++) {
                        if (x < 0 || x >= H || y < 0 || y >= W) {
                            continue;
                        }
                        if (S[x][y] == '#') {
                            count++;
                        }
                    }
                }
                cout << count;
            }
        }
        cout << endl;
    }
}
