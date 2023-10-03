#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int max1 = 0;
    int max2 = 0;
    int index1 = 0;
    int index2 = 0;
    vector<int> A(N);
    for (int i=0;i<N;i++) {
        cin >> A[i];
        if (A[i] > max1) {
            max2 = max1;
            index2 = index1;
            max1 = A[i];
            index1 = i;
        } else if (A[i] > max2) {
            max2 = A[i];
            index2 = i;
        }
    }
    for (int i=0;i<N;i++) {
        if (i == index1) {
            cout << max2 << endl;
        } else {
            cout << max1 << endl;
        }
    }
}
