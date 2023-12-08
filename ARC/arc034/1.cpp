#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    double ret=0;
    double a,b,c,d,e;
    for (int i=0;i<N;i++) {
        cin >> a >> b >> c >> d >> e;
        ret = max(ret, a+b+c+d+e*110/900);
    }
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
