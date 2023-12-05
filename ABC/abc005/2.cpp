#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret=100;
    for (int i=0;i<N;i++) {
        int T;
        cin >> T;
        ret=min(ret,T);
    }
    cout << ret << endl;
}
