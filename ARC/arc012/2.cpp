#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,a,b;
    double L;
    cin >> N >> a >> b >> L;
    for (int i=0;i<N;i++) {
        L = L*b/a;
    }
    cout << fixed << setprecision(10);
    cout << L << endl;
}
