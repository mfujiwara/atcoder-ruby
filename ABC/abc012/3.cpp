#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    N = 2025 - N;
    for (int i=1; i<10; i++) {
        if (N%i == 0 && N/i < 10) {
            cout << i << " x " << N/i << endl;
        }
    }
}
