#include <bits/stdc++.h>
using namespace std;

int main() {
    int K;
    cin >> K;
    long long ret=0;
    for (int i=0;i<K;i++) {
        for (int j=0;j<K;j++) {
            for (int k=0;k<K;k++) {
                ret+=gcd(gcd(i+1,j+1),k+1);
            }
        }
    }
    cout << ret << endl;
}
