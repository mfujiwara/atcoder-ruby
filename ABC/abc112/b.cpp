#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,T;
    cin >> N >> T;
    int ret=100000;
    for (int i=0;i<N;i++) {
        int c,t;
        cin >> c >> t;
        if (t<=T) {
            ret=min(ret,c);
        }
    }
    if (ret==100000) {
        cout << "TLE" << endl;
    } else {
        cout << ret << endl;
    }
}
