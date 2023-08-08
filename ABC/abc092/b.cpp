#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,D,X;
    cin >> N >> D >> X;
    int ret=0;
    for (int i=0;i<N;i++) {
        int A;
        cin >> A;
        ret += (D-1)/A+1;
    }
    cout << ret+X << endl;
}
