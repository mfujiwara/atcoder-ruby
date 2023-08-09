#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> A(N);
    int sum = 0;
    for (int i=0; i<N; i++) {
        cin >> A[i];
        sum += A[i];
    }
    int count = 0;
    for (int i=0; i<N; i++) {
        if (A[i]*4*M >= sum ) {
            count++;
        }
    }
    if (count >= M) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
