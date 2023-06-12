#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,X,L;
    cin >> N >> X;
    for (int i=0;i<N;i++) {
        cin >> L;
        X-=L;
        if (X<0) {
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << N+1 << endl;
}
