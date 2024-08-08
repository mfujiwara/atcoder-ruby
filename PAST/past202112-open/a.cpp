#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int H,W,h,w;
    cin >> H >> W >> h >> w;
    if (h>=H && w<=W) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
