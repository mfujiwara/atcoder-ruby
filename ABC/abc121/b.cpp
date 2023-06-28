#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M,C;
    cin >> N >> M >> C;
    vector<int> B(M);
    for (int i=0;i<M;i++) {
        cin >> B[i];
    }
    int ret=0;
    for (int i=0;i<N;i++) {
        int tmp=0;
        for (int j=0;j<M;j++) {
            int a;
            cin >> a;
            tmp+=a*B[j];
        }
        if (tmp+C>0) {
            ret++;
        }
    }
    cout << ret << endl;
}
