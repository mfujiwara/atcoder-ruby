#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A,B,V,W,T;
    cin >> A >> V >> B >> W >> T;
    if (V > W && abs(A-B) <= (V-W)*T) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
