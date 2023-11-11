#include <bits/stdc++.h>
using namespace std;

int main() {
    int H,W;
    cin >> H >> W;
    if (H*3 == W*4) {
        cout << "4:3" << endl;
    } else {
        cout << "16:9" << endl;
    }
}
