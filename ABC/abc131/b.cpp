#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,L;
    cin >> N >> L;
    int total=(L+L+N-1)*N/2;
    if (L>0) {
        cout << total-L << endl;
    } else if (L+N-1<0) {
        cout << total-(L+N-1) << endl;
    } else {
        cout << total << endl;
    }
}
