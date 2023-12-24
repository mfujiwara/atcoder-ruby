#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long ret=0;
    for (int i=0;i<N;i++) {
        long long A;
        cin >> A;
        ret += A*pow(2,(N-i-1));
    }
    cout << ret << endl;
}
