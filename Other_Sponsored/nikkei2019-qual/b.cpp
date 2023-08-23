#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string A,B,C;
    cin >> N >> A >> B >> C;
    int ret=0;
    for (int i=0;i<N;i++) {
        if (A[i]==B[i] && B[i]==C[i]) {
            continue;
        } else if (A[i]==B[i] || B[i]==C[i] || C[i]==A[i]) {
            ret++;
        } else {
            ret+=2;
        }
    }
    cout << ret << endl;
}
