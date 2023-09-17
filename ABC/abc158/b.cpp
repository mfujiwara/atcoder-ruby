#include <bits/stdc++.h>
using namespace std;

int main() {
    unsigned long long N,A,B;
    cin >> N >> A >> B;
    unsigned long long c=N/(A+B);
    unsigned long long d=N%(A+B);
    unsigned long long ret=c*A;
    if (d<=A) {
        ret+=d;
    } else {
        ret+=A;
    }
    cout << ret << endl;
}
