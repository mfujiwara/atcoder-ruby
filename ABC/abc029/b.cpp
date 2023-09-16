#include <bits/stdc++.h>
using namespace std;

int main() {
    int ret=0;
    for (int i=0;i<12;i++) {
        string s;
        cin >> s;
        if (s.find("r") != string::npos) {
            ret++;
        }
    }
    cout << ret << endl;
}
