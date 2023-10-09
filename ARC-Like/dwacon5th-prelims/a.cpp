#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    int total = 0;
    for (int i=0;i<N;i++) {
        cin >> A[i];
        total += A[i];
    }
    int diff=1000000000;
    int ret=-1;
    for (int i=0;i<N;i++) {
        int d=abs(total-N*A[i]);
        if (d<diff) {
            diff=d;
            ret=i;
        }
    }
    cout << ret << endl;
}
