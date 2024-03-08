#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int max = 0;
    int max2 = 0;
    for (int i=0;i<N;i++) {
        int A;
        cin >> A;
        if (A > max) {
            max2 = max;
            max = A;
        } else if (A!= max && A > max2) {
            max2 = A;
        }
    }
    cout << max2 << endl;
}
