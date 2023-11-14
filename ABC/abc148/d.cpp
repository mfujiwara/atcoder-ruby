#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int next = 1;
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        if (a == next) {
            next++;
        }
    }
    if (next == 1) {
        cout << -1 << endl;
    } else {
        cout << N - next + 1 << endl;
    }
}
