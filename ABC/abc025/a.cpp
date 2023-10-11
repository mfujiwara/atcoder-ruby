#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    int N;
    cin >> S >> N;
    for (int i=0;i<5;i++) {
        for (int j=0;j<5;j++) {
            if (i*5+j+1==N) {
                cout << S[i] << S[j] << endl;
                return 0;
            }
        }
    }
}
