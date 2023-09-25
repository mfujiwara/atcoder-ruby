#include <bits/stdc++.h>
using namespace std;

int main() {
    double Sx,Sy,Gx,Gy;
    cin >> Sx >> Sy >> Gx >> Gy;
    // (Sy+Gy):(Gx-Sx)=Sy:(ret-Sx)
    // (Sy+Gy)*(ret-Sx)=(Gx-Sx)*Sy
    // (Sy+Gy)*ret=(Gx-Sx)*Sy+(Sy+Gy)*Sx
    // ret=((Gx-Sx)*Sy+(Sy+Gy)*Sx)/(Sy+Gy)
    double ret= ((Gx-Sx)*Sy+(Sy+Gy)*Sx)/(Sy+Gy);
    cout << fixed << setprecision(10) << ret << endl;
}
