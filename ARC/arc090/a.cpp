#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> A(2, vector<int>(N));
    int tmp;
    for (int i=0;i<2;i++) {
        for (int j=0;j<N;j++) {
            cin >> tmp;
            if (i==0 && j==0) {
                A[i][j] = tmp;
            } else if (i==0) {
                A[i][j] = A[i][j-1] + tmp;
            } else if (j==0) {
                A[i][j] = tmp + A[i-1][j];
            } else {
                A[i][j] = max(A[i][j-1],A[i-1][j]) + tmp;
            }
        }
    }
    cout << A[1][N-1] << endl;
}
