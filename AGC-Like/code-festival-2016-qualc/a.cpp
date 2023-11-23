#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int progress = 0;
    for (int i=0;i<S.size();i++) {
        char c = S[i];
        if (c == 'C' && progress == 0) {
            progress++;
        } else if (c == 'F' && progress == 1) {
            progress++;
        }
    }
    if (progress == 2) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
