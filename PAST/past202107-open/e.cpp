#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long N;
    cin >> N;
    vector<long long> A(30,1);
    for (int i=0;i<30;i++) {
        for (int j=0;j<30;j++) {
            A[j]*=3;
        }
        A[i]+=1;
    }
    for (int i=0;i<30;i++) {
        if (N==A[i]) {
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
}
