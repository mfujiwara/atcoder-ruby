#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,K;
    cin >> A >> B >> K;
    int count = 0;
    for (int i=min(A,B);i>=1;i--) {
        if (A%i==0 && B%i==0) {
            count++;
            if (count==K) {
                cout << i << endl;
                return 0;
            }
        }
    }
}
