#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0;i<N;i++) {
        cin>>A[i];
        A[i]-=1;
    }
    vector<int> rets(N,0);
    for (int i=0;i<N;i++) {
        int j = i;
        int ret = 1;
        while (A[j] != i) {
            j = A[j];
            ret++;
        }
        rets[i] = ret;
    }
    for (int i=0;i<N;i++) {
        cout << rets[i];
        if (i != N-1) {
            cout << " ";
        } else {
            cout << endl;
        } 
    }
}
