#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N+1);
    for (int i=0;i<N+1;i++) {
        cin>>A[i];
    }
    long long ret = 0;
    for (int i=0;i<N;i++) {
        long long B;
        cin >> B;
        if (A[i] >= B) {
            ret += B;
        } else {
            ret += A[i];
            B -= A[i];
            if (A[i+1] >= B) {
                ret += B;
                A[i+1] -= B;
            } else {
                ret += A[i+1];
                A[i+1] = 0;
            }
        }
    }
    cout << ret << endl;
}
