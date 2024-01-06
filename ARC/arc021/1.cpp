#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int>> A(4, vector<int>(4));
    int tmp;
    for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++) {
            cin >> tmp;
            A[i][j] = tmp;
            if (i!=0) {
                if (A[i-1][j] == A[i][j]) {
                    cout << "CONTINUE" << endl;
                    return 0;
                }
            }
            if (j!=0) {
                if (A[i][j-1] == A[i][j]) {
                    cout << "CONTINUE" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "GAMEOVER" << endl;
}
