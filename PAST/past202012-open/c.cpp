#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    string ret = "";
    while (N > 0) {
        int d = N % 36;
        if (d < 10) {
            ret = to_string(d) + ret;
        } else {
            ret = (char)('A' + d - 10) + ret;
        }
        N /= 36;
    }
    if (ret == "") {
        cout << "0" << endl;
    } else {
        cout << ret << endl;
    }
}
