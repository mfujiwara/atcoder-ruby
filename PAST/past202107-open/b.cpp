#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    double A,B,C;
    cin >> A >> B >> C;
    while (A>B*C){
        A-=1;
    }
    double ret = min(A,B*C)/B;
    cout << fixed << setprecision(10);
    cout << ret << endl;
}
