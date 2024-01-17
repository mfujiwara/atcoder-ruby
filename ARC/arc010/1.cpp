#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M,A,B;
    cin >> N >> M >> A >> B;
    int c;
    for (int i=0;i<M;i++) {
        cin >> c;
        if (N<=A) {
            N += B;
        }
        N -= c;
        if (N<0) {
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << "complete" << endl;
}
