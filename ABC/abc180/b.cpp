#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long  m=0,e=0,c=0;
    for (int i=0;i<N;i++) {
        long long  x;
        cin>>x;
        m+=abs(x);
        e+=x*x;
        c=max(c,abs(x));
    }
    cout << m << endl;
    cout << fixed << setprecision(15) << sqrt(e) << endl;
    cout << fixed << setprecision(0) << c << endl;
}
