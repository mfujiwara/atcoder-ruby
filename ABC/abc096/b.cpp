#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C,K;
    cin >> A >> B >> C >> K;
    int maxi = max(max(A,B),C);
    int tmp=maxi;
    for (int i=0;i<K;i++) {
        tmp *= 2;
    }
    cout << A+B+C-maxi+tmp << endl;
}
