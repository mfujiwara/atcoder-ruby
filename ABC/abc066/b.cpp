#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int i = S.size() - 2; i >= 0; i -= 2) {
        string s = S.substr(0, i);
        if (s.substr(0, i / 2) == s.substr(i / 2, i / 2)) {
            cout << i << endl;
            return 0;
        }
    }
}
