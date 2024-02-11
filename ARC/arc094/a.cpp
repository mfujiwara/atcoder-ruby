#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    int maxi=max({A,B,C});
    int ret=3*maxi-A-B-C;
    if (ret%2==0) {
        cout << ret/2 << endl;
    } else {
        cout << (ret+3)/2 << endl;
    }
}
