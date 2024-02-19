#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<char>> s(N, vector<char>(N));
    for (int i=0;i<N;i++) {
        string tmp;
        cin >> tmp;
        for (int j=0;j<N;j++) {
            s[i][j] = tmp[j];
        }
    }
    for (int i=0;i<N;i++) {
        for (int j=N-1;j>=0;j--) {
            cout << s[j][i];
        }
        cout << endl;
    }
}
