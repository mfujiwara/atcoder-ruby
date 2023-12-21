#include <bits/stdc++.h>
using namespace std;

int main() {
    long long H,W;
    cin >> H >> W;
    if (H==1 || W==1) {
        cout << 1 << endl;
        return 0;
    }
    long long ret = ((H+1)/2) * ((W+1)/2) + (H/2) * (W/2);
    cout << ret << endl;
}
