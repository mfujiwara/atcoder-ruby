#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B;
    double H,M;
    cin >> A >> B >> H >> M;
    H = H + M/60;
    double theta = abs(30*H - 6*M);
    if (theta > 180) {
        theta = 360 - theta;
    }
    double ret = sqrt(A*A + B*B - 2*A*B*cos(theta*M_PI/180));
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
