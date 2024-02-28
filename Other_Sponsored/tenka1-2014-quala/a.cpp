#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> s(1000);
    for (int i=0;i<1000;i++) {
        s[i] = to_string(i+1);
    }
    sort(s.begin(), s.end());
    for (int i=0;i<1000;i++) {
        cout << s[i] << endl;
    }
}
