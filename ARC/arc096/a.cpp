#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C,X,Y;
    cin >> A >> B >> C >> X >> Y;
    // AB
    int ret0 = A*X + B*Y;
    // AC
    int ret1 = A*X + C*2*Y;
    // BC
    int ret2 = B*Y + C*2*X;
    // C
    int ret3 = C*2*max(X,Y);
    // CA CB
    int ret4 = C*2*min(X,Y) + A*(X-min(X,Y)) + B*(Y-min(X,Y));
    
    cout << min({ret0,ret1,ret2,ret3,ret4}) << endl;
}
