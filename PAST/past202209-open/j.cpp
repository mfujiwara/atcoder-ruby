#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    double H,W,D;
    cin >> H >> W >> D;
    if (H > W) {
        swap(H, W);
    }
    double rect = H*W;
    cout << fixed << setprecision(10);
    if (H>=2*D) {
        cout << D*D*3.14159265358979323846/rect << endl;
    } else if (H*H+W*W<=4*D*D) {
        cout << 1.0 << endl;
    } else if (H<2*D && W>=2*D) {
        double theta = acos(H/2/D);
        double S = D*D*(3.14159265358979323846-theta*2);
        double S2 = D*H*sin(theta);
        cout << (S+S2)/rect << endl;
    } else {
        double theta = acos(H/2/D);
        double theta2 = acos(W/2/D);
        double S = D*D*(3.14159265358979323846-theta*2-theta2*2);
        double S1 = D*H*sin(theta);
        double S2 = D*W*sin(theta2);
        cout << (S+S1+S2)/rect << endl;
    }
}
