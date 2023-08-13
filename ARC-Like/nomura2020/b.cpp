#include <bits/stdc++.h>
using namespace std;

int main() {
    string T;
    cin >> T;
    for (int i=0;i<T.size();i++) {
        char c = T[i];
        if (c == '?') {
            T[i] = 'D';
        }
    }
    cout << T << endl;
}
