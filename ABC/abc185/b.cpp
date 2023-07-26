#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M,T;
    cin >> N >> M >> T;
    int now=0;
    int n=N;
    for (int i=0;i<M;i++) {
        int A,B;
        cin >> A >> B;
        n-=A-now;
        if (n<=0) {
            cout << "No" << endl;
            return 0;
        }
        n=min(n+B-A,N);
        now=B;
    }
    n-=T-now;
    if (n<=0) {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
}
