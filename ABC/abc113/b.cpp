#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,T,A;
    cin >> N >> T >> A;
    T*=1000;
    A*=1000;
    int ret=0;
    int min=1000000000;
    for (int i=0;i<N;i++) {
        int H;
        cin >> H;
        int tmp=abs(A-(T-H*6));
        if (tmp<min) {
            min=tmp;
            ret=i+1;
        }
    }
    cout << ret << endl;
}
