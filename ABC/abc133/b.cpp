#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,D;
    cin >> N >> D;
    vector<vector<int>> X(N, vector<int>(D));
    int tmp;
    for (int i=0;i<N;i++) {
        for (int j=0;j<D;j++) {
            cin >> tmp;
            X[i][j] = tmp;
        }
    }
    int ret=0;
    for (int i=0;i<N-1;i++) {
        for (int j=i+1;j<N;j++) {
            int d2=0;
            for (int k=0;k<D;k++) {
                int d=X[i][k]-X[j][k];
                d2+=d*d;
            }
            int d=sqrt(d2);
            if (d*d==d2) {
                ret++;
            }
        }
    }
    cout << ret << endl;
}
