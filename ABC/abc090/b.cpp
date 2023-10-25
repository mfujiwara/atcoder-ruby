#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B;
    cin >> A >> B;
    int ret=0;
    for (int i=A;i<=B;i++) {
        string s = to_string(i);
        if (s[0]==s[4] && s[1]==s[3]) {
            ret++;
        }
    }
    cout << ret << endl;
}
