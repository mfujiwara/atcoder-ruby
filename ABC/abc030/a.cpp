#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C,D;
    cin >> A >> B >> C >> D;
    if (B*C>D*A) {
        cout << "TAKAHASHI" << endl;
    } else if (B*C<D*A) {
        cout << "AOKI" << endl;
    } else {
        cout << "DRAW" << endl;
    }
}
