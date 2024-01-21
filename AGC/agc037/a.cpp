#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    string pre = "";
    string cur = "";
    int ret = 0;
    for (int i=0;i<S.size();i++) {
        cur += S[i];
        if (pre != cur) {
            ret++;
            pre = cur;
            cur = "";
        }
    }
    cout << ret << endl;
}
