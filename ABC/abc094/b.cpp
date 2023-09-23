#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M,X;
    cin >> N >> M >> X;
    int low=0;
    int high=0;
    for (int i=0;i<M;i++) {
        int A;
        cin >> A;
        if (A<X) {
            low++;
        } else {
            high++;
        }
    }
    cout << min(low,high) << endl;
}
