#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long maxA=0, maxB=0;
    for (int i=0;i<N;i++) {
        long long A,B;
        cin >> A >> B;
        if (maxA < A) {
            maxA = A;
            maxB = B;
        }
    }
    cout << maxA+maxB << endl;
}
