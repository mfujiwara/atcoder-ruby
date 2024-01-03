#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,Q;
    cin >> N >> Q;
    int L,R;
    long long T;
    vector<long long> A(N);
    for (int i=0;i<Q;i++) {
        cin >> L >> R >> T;
        for (int j=L-1;j<R;j++) {
            A[j] = T;
        }
    }
    for (int i=0;i<N;i++) {
        cout << A[i] << endl;
    }
}
