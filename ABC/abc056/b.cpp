#include <bits/stdc++.h>
using namespace std;

int main() {
    int W,a,b;
    cin >> W >> a >> b;
    if (a<=b && b<=a+W) {
        cout << 0 << endl;
    } else if (b<=a && a<=b+W) {
        cout << 0 << endl;
    } else {
        cout << min(abs(a-b-W), abs(b-a-W)) << endl;
    }
}
