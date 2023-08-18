#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    int ret=1;
    for (int i=0;i<N;i++) {
        if (ret*2<ret+K) {
            ret*=2;
        } else {
            ret+=K;
        }
    }
    cout << ret << endl;
}
