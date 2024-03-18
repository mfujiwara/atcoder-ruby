#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> rets(N, 0);
    for (int x=1;x<=100;x++) {
        for (int y=1;y<=100;y++) {
            for (int z=1;z<=100;z++) {
                int ret = x*x + y*y + z*z + x*y + y*z + z*x;
                if (ret <= N) {
                    rets[ret-1]++;
                }
            }
        }
    }
    for (int i=0;i<N;i++) {
        cout << rets[i] << endl;
    }
}
