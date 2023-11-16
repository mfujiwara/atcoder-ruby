#include <bits/stdc++.h>
using namespace std;

int main() {
    int A;
    cin >> A;
    for (int i=1;i<101;i++) {
        if (i*i*i==A) {
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}
