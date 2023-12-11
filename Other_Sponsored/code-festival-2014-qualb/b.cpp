#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    int tmp;
    for (int i=1;i<=N;i++) {
        cin >> tmp;
        K-=tmp;
        if (K<=0) {
            cout << i << endl;
            return 0;
        }
    }
}
