#include <bits/stdc++.h>
using namespace std;

int main() {
    int x,y,k;
    cin >> x >> y >> k;
    if (y>=k) {
        cout << x+k << endl;
    } else {
        cout << x+y-(k-y) << endl;
    }
}
