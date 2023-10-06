#include <bits/stdc++.h>
using namespace std;

int main() {
    long A,B,C;
    cin >> A >> B >> C;
    int MOD=998244353;
    long x=(A*(A+1)/2)%MOD;
    long y=(B*(B+1)/2)%MOD;
    long z=(C*(C+1)/2)%MOD;
    cout << (x*y%MOD)*z%MOD << endl;
}
