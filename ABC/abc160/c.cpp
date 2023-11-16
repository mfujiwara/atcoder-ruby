#include <bits/stdc++.h>
using namespace std;

int main() {
    int K,N;
    cin >> K >> N;
    vector<int> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    int ret=K;
    for (int i=0;i<N;i++) {
        ret=min(ret, A[(i-1+N)%N]-A[i]);
        A[i]+=K;
    }
    cout << ret << endl;
}
