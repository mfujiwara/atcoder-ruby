#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    double x1,y1,x2,y2;
    cin >> x1 >> y1 >> x2 >> y2;
    auto dx = (x2+x1)/2;
    auto dy = (y2+y1)/2;
    x1 -= dx;
    y1 -= dy;
    x2 -= dx;
    y2 -= dy;
    double d = sqrt(x1*x1+y1*y1);
    double x = -x1/d;
    double y = y1/d;
    
    cout << fixed << setprecision(10);
    for (int i=0;i<N;i++) {
        double a,b;
        cin >> a >> b;
        a -= dx;
        b -= dy;
        cout << a*x-b*y << " " << a*y+b*x << endl;
    }    
}
